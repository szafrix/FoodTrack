from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.repositories.product_repository import (
    ProductRepository,
    GetProductFromRepositoryInput,
)


class GetProductFromRepositoryUseCaseInput(BaseModel):
    product_name: str


class GetProductFromRepositoryUseCaseOutput(BaseModel):
    success: bool
    product: Product | None
    error: str | None


class GetProductFromRepositoryUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(
        self, input_: GetProductFromRepositoryUseCaseInput
    ) -> GetProductFromRepositoryUseCaseOutput:
        repository_query = GetProductFromRepositoryInput(
            product_name=input_.product_name
        )
        repository_response = self.product_repository.get_product(repository_query)
        return GetProductFromRepositoryUseCaseOutput(
            success=repository_response.success,
            product=repository_response.product,
            error=repository_response.error,
        )
