import pandas as pd
from src.core.services.analytics.service import (
    AnalyticsService,
    DailySumOfIntakesAnalyticsServiceInput,
    DailySumOfIntakesAnalyticsServiceOutput,
)
from src.core.services.analytics.exceptions import (
    DailySumOfIntakesAnalyticsServiceError,
)
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.product.repository import ProductRepository
from src.core.repositories.intake.models import GetIntakesByDateRepositoryInput
from logging import getLogger
from datetime import datetime
from src.core.repositories.product.models import GetProductsRepositoryInput

logger = getLogger(__name__)


class SqliteAnalyticsService(AnalyticsService):
    def __init__(
        self,
        intake_repository: IntakeRepository,
        product_repository: ProductRepository,
    ):
        super().__init__(intake_repository, product_repository)

    def get_sum_of_daily_intakes(
        self, input_: DailySumOfIntakesAnalyticsServiceInput
    ) -> DailySumOfIntakesAnalyticsServiceOutput:
        try:
            intakes = []
            for date in input_.dates:
                intakes_for_date = self.intake_repository.get_intakes_by_date(
                    GetIntakesByDateRepositoryInput(date=date)
                )
                intakes.extend(intakes_for_date.intakes)
            product_names_to_retrieve = [intake.product_name for intake in intakes]
            products = self.product_repository.get_products(
                GetProductsRepositoryInput(product_names=product_names_to_retrieve)
            )

            intakes_df = pd.DataFrame([intake.model_dump() for intake in intakes])
            products_df = pd.DataFrame(
                [product.model_dump() for product in products.products]
            )

            merged_df = intakes_df.merge(
                products_df, left_on="product_name", right_on="name"
            )
            merged_df["kcal"] = merged_df["quantity_g"] * merged_df["kcal_100g"] / 100
            merged_df["proteins"] = (
                merged_df["quantity_g"] * merged_df["proteins_100g"] / 100
            )
            merged_df["carbs"] = merged_df["quantity_g"] * merged_df["carbs_100g"] / 100
            merged_df["fats"] = merged_df["quantity_g"] * merged_df["fats_100g"] / 100
            merged_df["date"] = merged_df["date"].dt.date
            merged_df = merged_df.groupby("date").sum().reset_index()
            return DailySumOfIntakesAnalyticsServiceOutput(
                dates=merged_df["date"].tolist(),
                kcal_daily_intakes=merged_df["kcal"].tolist(),
                proteins_daily_intakes=merged_df["proteins"].tolist(),
                carbs_daily_intakes=merged_df["carbs"].tolist(),
                fats_daily_intakes=merged_df["fats"].tolist(),
            )
        except Exception as exc:
            raise DailySumOfIntakesAnalyticsServiceError(
                f"Error retrieving sum of daily intakes for analytics"
            ) from exc
