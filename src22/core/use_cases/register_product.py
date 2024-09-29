from src.adapters.repositories.product_repository import IProductRepository
from src.core.entities.requests.register_product_request import \
    RegisterProductRequest


class RegisterProduct:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def execute(self, fetch_product_request: RegisterProductRequest) -> None:
        self.product_repository.register_product(fetch_product_request)
