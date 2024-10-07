from logging import getLogger
from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.repositories.product.repository import ProductRepository
from src.core.repositories.product.models import SearchProductsForAutocompletionInput
from src.core.exceptions import BaseError, UnexpectedError

logger = getLogger(__name__)


class FetchProductsForAutocompletionUseCaseInput(BaseModel):
    user_input: str


class FetchProductsForAutocompletionUseCaseOutput(BaseModel):
    products: list[Product]


class FetchProductsForAutocompletionUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def fetch_products_for_autocompletion(
        self, input_: FetchProductsForAutocompletionUseCaseInput
    ) -> FetchProductsForAutocompletionUseCaseOutput:
        try:
            search_products_for_autocompletion_input = (
                SearchProductsForAutocompletionInput(
                    query=input_.user_input,
                )
            )
            search_products_for_autocompletion_output = (
                self.product_repository.search_products_for_autocompletion(
                    search_products_for_autocompletion_input
                )
            )
            return search_products_for_autocompletion_output
        except BaseError as exc:
            logger.error(
                exc,
                exc_info=True,
            )
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while fetching products for autocompletion {exc}",
                exc_info=True,
            )
            raise UnexpectedError(
                f"Unexpected error while fetching products for autocompletion"
            ) from exc
