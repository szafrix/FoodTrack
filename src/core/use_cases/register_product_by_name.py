from src.core.domain.product import Product
from src.repositories.product_repository import IProductRepository
from src.rest_api.api import RegisterProductByNameRequest


class RegisterProductByNameInput:
    product_name: str

    @classmethod
    def from_request(cls, request: RegisterProductByNameRequest):
        return cls(product_name=request.product_name)


class RegisterProductByNameOutput:
    product_name: str


class RegisterProductByName:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def execute(
        self, input_: RegisterProductByNameInput
    ) -> RegisterProductByNameOutput:
        product = self.product_repository.register_product_by_name(input_.product_name)
        return RegisterProductByNameOutput(product_name=product.product_name)
