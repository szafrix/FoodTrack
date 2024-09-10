from src.intake.base import Intake
from src.products.base import Product
from src.database.database import insert_intake, insert_product


def record_intake(
    product: Product,
    quantity_g: float,
    meal_type: str,
    intake_datetime: str | None = None,
) -> None:
    insert_product(product)
    intake = Intake.from_product(product, quantity_g, meal_type, intake_datetime)
    insert_intake(intake)
