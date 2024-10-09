from abc import ABC, abstractmethod
from pydantic import BaseModel
from datetime import datetime
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.product.repository import ProductRepository


class DailySumOfIntakesAnalyticsServiceInput(BaseModel):
    dates: list[datetime]


class DailySumOfIntakesAnalyticsServiceOutput(BaseModel):
    dates: list[datetime]
    kcal_daily_intakes: list[float]
    fats_daily_intakes: list[float]
    carbs_daily_intakes: list[float]
    proteins_daily_intakes: list[float]


class AnalyticsService(ABC):
    def __init__(
        self, intake_repository: IntakeRepository, product_repository: ProductRepository
    ):
        self.intake_repository = intake_repository
        self.product_repository = product_repository

    @abstractmethod
    def get_sum_of_daily_intakes(
        self, input_: DailySumOfIntakesAnalyticsServiceInput
    ) -> DailySumOfIntakesAnalyticsServiceOutput:
        pass
