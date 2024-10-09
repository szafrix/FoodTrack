from pydantic import BaseModel
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.product.repository import ProductRepository
from logging import getLogger
from src.core.services.analytics.service import AnalyticsService
from datetime import datetime
from src.core.exceptions import BaseError, UnexpectedError

logger = getLogger(__name__)


class RetrieveSumOfDailyIntakesForAnalyticsUseCaseInput(BaseModel):
    dates: list[datetime]


class RetrieveSumOfDailyIntakesForAnalyticsUseCaseOutput(BaseModel):
    dates: list[datetime]
    kcal_daily_intakes: list[float]
    fats_daily_intakes: list[float]
    carbs_daily_intakes: list[float]
    proteins_daily_intakes: list[float]


class RetrieveSumOfDailyIntakesForAnalyticsUseCase:
    def __init__(
        self,
        analytics_service: AnalyticsService,
    ):
        self.analytics_service = analytics_service

    def execute(
        self, input_: RetrieveSumOfDailyIntakesForAnalyticsUseCaseInput
    ) -> RetrieveSumOfDailyIntakesForAnalyticsUseCaseOutput:
        try:
            sum_of_daily_intakes = self.analytics_service.get_sum_of_daily_intakes(
                input_.dates
            )
            return RetrieveSumOfDailyIntakesForAnalyticsUseCaseOutput(
                dates=sum_of_daily_intakes.dates,
                kcal_daily_intakes=sum_of_daily_intakes.kcal_daily_intakes,
                fats_daily_intakes=sum_of_daily_intakes.fats_daily_intakes,
                carbs_daily_intakes=sum_of_daily_intakes.carbs_daily_intakes,
                proteins_daily_intakes=sum_of_daily_intakes.proteins_daily_intakes,
            )
        except BaseError as exc:
            logger.error(exc, exc_info=True)
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while retrieving sum of daily intakes for analytics {exc}",
                exc_info=True,
            )
