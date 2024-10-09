from pydantic import BaseModel
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.product.repository import ProductRepository
from logging import getLogger
from src.core.services.analytics.service import AnalyticsService
from datetime import datetime
from src.core.exceptions import BaseError, UnexpectedError
from src.core.services.analytics.service import (
    DailySumOfIntakesAnalyticsServiceInput,
)

logger = getLogger(__name__)


class GetDailySumOfIntakesUseCaseInput(BaseModel):
    dates: list[datetime]


class GetDailySumOfIntakesUseCaseOutput(BaseModel):
    dates: list[datetime]
    kcal_daily_intakes: list[float]
    fats_daily_intakes: list[float]
    carbs_daily_intakes: list[float]
    proteins_daily_intakes: list[float]


class GetDailySumOfIntakesUseCase:
    def __init__(
        self,
        analytics_service: AnalyticsService,
    ):
        self.analytics_service = analytics_service

    def execute(
        self, input_: GetDailySumOfIntakesUseCaseInput
    ) -> GetDailySumOfIntakesUseCaseOutput:
        try:
            logger.error(input_)
            analytics_input = DailySumOfIntakesAnalyticsServiceInput(dates=input_.dates)
            analytics_output = self.analytics_service.get_sum_of_daily_intakes(
                analytics_input
            )

            return GetDailySumOfIntakesUseCaseOutput(
                dates=analytics_output.dates,
                kcal_daily_intakes=analytics_output.kcal_daily_intakes,
                fats_daily_intakes=analytics_output.fats_daily_intakes,
                carbs_daily_intakes=analytics_output.carbs_daily_intakes,
                proteins_daily_intakes=analytics_output.proteins_daily_intakes,
            )
        except BaseError as exc:
            logger.error(exc, exc_info=True)
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while retrieving sum of daily intakes for analytics {exc}",
                exc_info=True,
            )
