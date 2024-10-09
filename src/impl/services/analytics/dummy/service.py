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
from logging import getLogger
from datetime import datetime

logger = getLogger(__name__)


class DummyAnalyticsService(AnalyticsService):
    def __init__(
        self,
        intake_repository: IntakeRepository,
        product_repository: ProductRepository,
    ):
        super().__init__(intake_repository, product_repository)

    def get_sum_of_daily_intakes(
        self, input_: DailySumOfIntakesAnalyticsServiceInput
    ) -> DailySumOfIntakesAnalyticsServiceOutput:
        return DailySumOfIntakesAnalyticsServiceOutput(
            dates=input_.dates,
            kcal_daily_intakes=[1000] * len(input_.dates),
            fats_daily_intakes=[100] * len(input_.dates),
            carbs_daily_intakes=[100] * len(input_.dates),
            proteins_daily_intakes=[100] * len(input_.dates),
        )
