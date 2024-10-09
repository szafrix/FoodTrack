from abc import ABC, abstractmethod
from src.core.repositories.product.models import (
    SearchProductsForAutocompletionInput,
    SearchProductsForAutocompletionOutput,
    SaveProductToRepositoryInput,
    SaveProductToRepositoryOutput,
    GetProductsRepositoryInput,
    GetProductsRepositoryOutput,
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

    @abstractmethod
    def get_products(
        self, input_: GetProductsRepositoryInput
    ) -> GetProductsRepositoryOutput:
        pass
