from dataclasses import dataclass
from typing import Optional
from src.repositories.product_repository import IProductRepository


@dataclass
class RegisterProductByBarcodeInput:
    barcode: str


@dataclass
class RegisterProductByBarcodeOutput:
    barcode: str
    product_name: str


class RegisterProductByBarcode:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def execute(
        self, input_data: RegisterProductByBarcodeInput
    ) -> RegisterProductByBarcodeOutput:
        product = self.product_repository.register_product_by_barcode(
            input_data.barcode
        )
        return RegisterProductByBarcodeOutput(
            barcode=product.barcode,
            product_name=product.product_name,
        )
