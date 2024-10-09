from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.entities.intake import Intake
from datetime import datetime


class GetIntakesByDateRepositoryInput(BaseModel):
    date: datetime


class GetIntakesByDateRepositoryOutput(BaseModel):
    intakes: list[Intake]


class SaveIntakeToRepositoryInput(BaseModel):
    product: Product
    quantity: int
    date: datetime


class SaveIntakeToRepositoryOutput(BaseModel):
    success: bool
    message: str
