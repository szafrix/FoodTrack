from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.repositories.product.repository import (
    ProductRepository,
    SaveProductToRepositoryInput,
)
from src.core.exceptions import BaseError, UnexpectedError
from logging import getLogger

logger = getLogger(__name__)


class RegisterProductInRepositoryUseCaseInput(BaseModel):
    product: Product


class RegisterProductInRepositoryUseCaseOutput(BaseModel):
    product: Product


class RegisterProductInRepositoryUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(
        self, input_: RegisterProductInRepositoryUseCaseInput
    ) -> RegisterProductInRepositoryUseCaseOutput:
        try:
            save_product_input = SaveProductToRepositoryInput(product=input_.product)
            repository_response = self.product_repository.save_product(
                save_product_input
            )
            return RegisterProductInRepositoryUseCaseOutput(
                product=repository_response.product,
            )
        except BaseError as exc:
            logger.error(exc, exc_info=True)
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while registering product in repository {exc}",
                exc_info=True,
            )
            raise UnexpectedError(
                f"Unexpected error while registering product in repository"
            ) from exc
