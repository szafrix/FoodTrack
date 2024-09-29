from typing import List
from abc import ABC, abstractmethod
import sqlite3

from src.core.entities.intake import Intake
from typing import Union, Optional
from src.core.entities.requests.fetch_product_requests import RegisterIntakeRequest


class RegisterIntakeRepositoryRequest:
    product_name: str
    quantity: float
    meal_type: str
    date: str


class RegisterIntakeRepositoryResponse:
    intake_id: int
    product_name: str
    quantity: float
    meal_type: str
    date: str


class IIntakeRepository(ABC):
    @abstractmethod
    def register_intake(
        self, input_data: RegisterIntakeRepositoryRequest
    ) -> RegisterIntakeRepositoryResponse:
        pass
