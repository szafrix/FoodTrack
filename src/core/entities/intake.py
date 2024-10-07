from datetime import datetime
from pydantic import BaseModel


class Intake(BaseModel):
    product_name: str
    quantity_g: float
    date: datetime
