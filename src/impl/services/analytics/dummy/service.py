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
from logging import getLogger
from datetime import datetime

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
        return SumOfDailyIntakesAnalyticsServiceOutput(
            dates=input_.dates,
            kcal_daily_intakes=[],
            fats_daily_intakes=[],
            carbs_daily_intakes=[],
            proteins_daily_intakes=[],
        )
