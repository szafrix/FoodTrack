from pydantic import BaseModel, Field


class Product(BaseModel):
    id_: int | None = Field(
        default=None, description="Unique identifier for the product"
    )
    name: str
    kcal_100g: float
    proteins_100g: float
    carbs_100g: float
    fats_100g: float

    def __str__(self):
        return self.name
