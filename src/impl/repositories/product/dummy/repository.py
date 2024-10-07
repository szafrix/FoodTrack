from core.repositories.product.models import (
    SearchProductsForAutocompletionInput,
    SearchProductsForAutocompletionOutput,
    SaveProductToRepositoryInput,
    SaveProductToRepositoryOutput,
)

from src.core.repositories.product.repository import ProductRepository
from src.core.entities.product import Product


class DummyProductRepository(ProductRepository):
    def search_products_for_autocompletion(
        self, input_: SearchProductsForAutocompletionInput
    ) -> SearchProductsForAutocompletionOutput:
        return SearchProductsForAutocompletionOutput(
            products=[
                Product(
                    name="Product 1",
                    kcal_100g=100,
                    proteins_100g=10,
                    carbs_100g=10,
                    fats_100g=10,
                ),
                Product(
                    name="Product 2",
                    kcal_100g=200,
                    proteins_100g=20,
                    carbs_100g=20,
                    fats_100g=20,
                ),
            ]
        )

    def save_product(
        self, input_: SaveProductToRepositoryInput
    ) -> SaveProductToRepositoryOutput:
        return SaveProductToRepositoryOutput(
            product=Product(
                name="Product 1",
                kcal_100g=100,
                proteins_100g=10,
                carbs_100g=10,
                fats_100g=10,
            )
        )
