from abc import ABC, abstractmethod
from src.core.repositories.product.models import (
    SearchProductsForAutocompletionInput,
    SearchProductsForAutocompletionOutput,
    SaveProductToRepositoryInput,
    SaveProductToRepositoryOutput,
)


class ProductRepository(ABC):
    @abstractmethod
    def search_products_for_autocompletion(
        self, input_: SearchProductsForAutocompletionInput
    ) -> SearchProductsForAutocompletionOutput:
        pass

    @abstractmethod
    def save_product(
        self, input_: SaveProductToRepositoryInput
    ) -> SaveProductToRepositoryOutput:
        pass
