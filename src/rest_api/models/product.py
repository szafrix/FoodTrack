from pydantic import BaseModel
from src.core.use_cases.register_product_by_name import RegisterProductByNameOutput
from src.core.use_cases.register_product_by_barcode import (
    RegisterProductByBarcodeOutput,
)


class RegisterProductByNameRequest(BaseModel):
    product_name: str


class RegisterProductByNameResponse(BaseModel):
    product_name: str

    @classmethod
    def from_use_case_response(cls, use_case_response: RegisterProductByNameOutput):
        return cls(product_name=use_case_response.product_name)


class RegisterProductByBarcodeRequest(BaseModel):
    barcode: str


class RegisterProductByBarcodeResponse(BaseModel):
    barcode: str
    product_name: str

    @classmethod
    def from_use_case_response(cls, use_case_response: RegisterProductByBarcodeOutput):
        return cls(
            barcode=use_case_response.barcode,
            product_name=use_case_response.product_name,
        )
