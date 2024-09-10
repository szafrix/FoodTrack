from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class Product:
    name: str
    ean_code: str
    energy_kcal_100g: float
    quantity_g: float
    brand: str = ""
    tags: str = ""
    carbohydrates_100g: float = 0.0
    fat_100g: float = 0.0
    proteins_100g: float = 0.0
    fiber_100g: float = 0.0
    salt_100g: float = 0.0
    saturated_fat_100g: float = 0.0
    sodium_100g: float = 0.0
    sugars_100g: float = 0.0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            ean_code=data["ean_code"],
            energy_kcal_100g=data["energy_kcal_100g"],
            quantity_g=data["quantity_g"],
            brand=data.get("brand", ""),
            tags=data.get("tags", ""),
            carbohydrates_100g=data.get("carbohydrates_100g", 0.0),
            fat_100g=data.get("fat_100g", 0.0),
            proteins_100g=data.get("proteins_100g", 0.0),
            fiber_100g=data.get("fiber_100g", 0.0),
            salt_100g=data.get("salt_100g", 0.0),
            saturated_fat_100g=data.get("saturated_fat_100g", 0.0),
            sodium_100g=data.get("sodium_100g", 0.0),
            sugars_100g=data.get("sugars_100g", 0.0),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def __str__(self) -> str:
        return f"{self.name} ({self.brand})"

    def __repr__(self) -> str:
        return f"Product(name={self.name}, brand={self.brand}, quantity={self.quantity_g} ean_code={self.ean_code})"

    def print_detailed_info_in_tabular_format(self) -> str:
        return f"""
| **Attribute**         | **Value**                        |
|-----------------------|----------------------------------|
| **Name**              | {self.name}                      |
| **Brand**             | {self.brand}                     |
| **EAN code**          | {self.ean_code}                  |
| **Quantity**          | {self.quantity_g} g              |
| **Tags**              | {self.tags}                      |
| **Energy**            | {self.energy_kcal_100g} kcal/100g|
| **Carbohydrates**     | {self.carbohydrates_100g} g/100g |
| **Fat**               | {self.fat_100g} g/100g           |
| **Proteins**          | {self.proteins_100g} g/100g      |
| **Fiber**             | {self.fiber_100g} g/100g         |
| **Salt**              | {self.salt_100g} g/100g          |
| **Saturated fat**     | {self.saturated_fat_100g} g/100g |
| **Sodium**            | {self.sodium_100g} g/100g        |
| **Sugars**            | {self.sugars_100g} g/100g        |
    """
