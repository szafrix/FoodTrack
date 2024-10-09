import pandas as pd
from src.core.services.analytics.service import (
    AnalyticsService,
    SumOfDailyIntakesAnalyticsServiceInput,
    SumOfDailyIntakesAnalyticsServiceOutput,
)
from src.core.services.analytics.exceptions import (
    SumOfDailyIntakesAnalyticsServiceError,
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
        self, input_: SumOfDailyIntakesAnalyticsServiceInput
    ) -> SumOfDailyIntakesAnalyticsServiceOutput:
        try:
            intakes = []
            for date in input_.dates:
                intakes.extend(
                    self.intake_repository.get_intakes_by_date(
                        GetIntakesByDateRepositoryInput(date=date)
                    )
                )

            product_ids_to_retrieve = [intake.product_id for intake in intakes]
            products = self.product_repository.get_products(
                GetProductsRepositoryInput(product_ids=product_ids_to_retrieve)
            )

            intakes_df = pd.DataFrame(intakes.model_dump())
            products_df = pd.DataFrame(products.model_dump())

            merged_df = intakes_df.merge(
                products_df, left_on="product_name", right_on="name"
            )
            merged_df["kcal"] = merged_df["quantity_g"] * merged_df["kcal_100g"] / 100
            merged_df["proteins"] = (
                merged_df["quantity_g"] * merged_df["proteins_100g"] / 100
            )
            merged_df["carbs"] = merged_df["quantity_g"] * merged_df["carbs_100g"] / 100
            merged_df["fats"] = merged_df["quantity_g"] * merged_df["fats_100g"] / 100
            merged_df = merged_df.groupby("date").sum().reset_index()

            return SumOfDailyIntakesAnalyticsServiceOutput(
                dates=merged_df["date"].tolist(),
                kcal_daily_intakes=merged_df["kcal"].tolist(),
                proteins_daily_intakes=merged_df["proteins"].tolist(),
                carbs_daily_intakes=merged_df["carbs"].tolist(),
                fats_daily_intakes=merged_df["fats"].tolist(),
            )
        except Exception as exc:
            raise SumOfDailyIntakesAnalyticsServiceError(
                f"Error retrieving sum of daily intakes for analytics"
            ) from exc
