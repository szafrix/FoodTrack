from dataclasses import dataclass, asdict
from typing import Any, Dict, List


@dataclass
class Product:
    name: str
    brand: str
    ean_code: str
    quantity_g: float
    tags: List[str]
    energy_kcal_100g: float
    carbohydrates_100g: float
    fat_100g: float
    proteins_100g: float
    fiber_100g: float
    salt_100g: float
    saturated_fat_100g: float
    sodium_100g: float
    sugars_100g: float

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            brand=data["brand"],
            ean_code=data["ean_code"],
            quantity_g=data["quantity_g"],
            tags=data["tags"],
            energy_kcal_100g=data["energy-kcal_100g"],
            carbohydrates_100g=data["carbohydrates_100g"],
            fat_100g=data["fat_100g"],
            proteins_100g=data["proteins_100g"],
            fiber_100g=data["fiber_100g"],
            salt_100g=data["salt_100g"],
            saturated_fat_100g=data["saturated-fat_100g"],
            sodium_100g=data["sodium_100g"],
            sugars_100g=data["sugars_100g"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def __str__(self) -> str:
        return f"{self.name} ({self.brand})"

    def __repr__(self) -> str:
        return f"Product(name={self.name}, brand={self.brand}, quantity={self.quantity_g} ean_code={self.ean_code})"
