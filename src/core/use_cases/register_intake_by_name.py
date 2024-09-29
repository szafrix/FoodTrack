from dataclasses import dataclass
from typing import Optional
from src.repositories.intake_repository import IIntakeRepository


@dataclass
class RegisterIntakeByNameInput:
    product_name: str
    quantity: float
    meal_type: str
    date: str


@dataclass
class RegisterIntakeByNameOutput:
    intake_id: int
    product_name: str
    quantity: float
    meal_type: str
    date: str


class RegisterIntakeByName:
    def __init__(self, intake_repository: IIntakeRepository):
        self.intake_repository = intake_repository

    def execute(
        self, input_data: RegisterIntakeByNameInput
    ) -> RegisterIntakeByNameOutput:
        intake = self.intake_repository.register_intake_by_name(input_data)
        return RegisterIntakeByNameOutput(
            intake_id=intake.intake_id,
            product_name=input_data.product_name,
            quantity=input_data.quantity,
            meal_type=input_data.meal_type,
            date=input_data.date,
        )
