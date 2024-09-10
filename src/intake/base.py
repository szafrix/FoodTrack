from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.products.base import Product


@dataclass
class Intake:
    ean_code: str
    name: str
    quantity_g: float
    intake_datetime: str
    meal_type: str
    energy_kcal: float
    carbohydrates_g: float
    fats_g: float
    proteins_g: float
    fiber_g: float
    salt_g: float
    saturated_fat_g: float
    sodium_g: float
    sugars_g: float

    @classmethod
    def from_product(
        cls,
        product: Product,
        quantity_g: float,
        meal_type: str,
        intake_datetime: Optional[str] = None,
    ) -> "Intake":
        if intake_datetime is None:
            intake_datetime = datetime.now()
            intake_datetime = intake_datetime.strftime("%Y-%m-%d %H:%M:%S")

        factor = quantity_g / 100.0
        return cls(
            ean_code=product.ean_code,
            name=product.name,
            quantity_g=quantity_g,
            intake_datetime=intake_datetime,
            meal_type=meal_type,
            energy_kcal=product.energy_kcal_100g * factor,
            carbohydrates_g=product.carbohydrates_100g * factor,
            fats_g=product.fat_100g * factor,
            proteins_g=product.proteins_100g * factor,
            fiber_g=product.fiber_100g * factor,
            salt_g=product.salt_100g * factor,
            saturated_fat_g=product.saturated_fat_100g * factor,
            sodium_g=product.sodium_100g * factor,
            sugars_g=product.sugars_100g * factor,
        )
