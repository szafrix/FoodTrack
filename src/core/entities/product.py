from pydantic import BaseModel


class Product(BaseModel):
    name: str
    kcal_100g: float
    proteins_100g: float
    carbs_100g: float
    fats_100g: float

    def __str__(self):
        return self.name

