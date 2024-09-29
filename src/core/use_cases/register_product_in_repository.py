from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.repositories.product_repository import (
    ProductRepository,
    SaveProductToRepositoryInput,
)


class RegisterProductInRepositoryUseCaseInput(BaseModel):
    product: Product


class RegisterProductInRepositoryUseCaseOutput(BaseModel):
    success: bool
    error: str | None


class RegisterProductInRepositoryUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(
        self, input_: RegisterProductInRepositoryUseCaseInput
    ) -> RegisterProductInRepositoryUseCaseOutput:
        repository_input = SaveProductToRepositoryInput(product=input_.product)
        repository_response = self.product_repository.save_product(repository_input)
        return RegisterProductInRepositoryUseCaseOutput(
            success=repository_response.success,
            error=repository_response.error,
        )
