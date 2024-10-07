from pydantic import BaseModel
from src.core.entities.product import Product
from datetime import datetime


class SaveIntakeToRepositoryInput(BaseModel):
    product: Product
    quantity: int
    date: datetime


class SaveIntakeToRepositoryOutput(BaseModel):
    success: bool
    message: str
