from src.core.repositories.product_repository import (
    ProductRepository,
    GetProductFromRepositoryInput,
    GetProductFromRepositoryOutput,
    SaveProductToRepositoryInput,
    SaveProductToRepositoryOutput,
)
from src.core.entities.product import Product


class DummyProductRepository(ProductRepository):
    def get_product(
        self, input_: GetProductFromRepositoryInput
    ) -> GetProductFromRepositoryOutput:
        product = Product(
            name="test", kcal_100g=100, proteins_100g=100, carbs_100g=100, fats_100g=100
        )
        return GetProductFromRepositoryOutput(success=True, product=product, error=None)

    def save_product(
        self, input_: SaveProductToRepositoryInput
    ) -> SaveProductToRepositoryOutput:
        return SaveProductToRepositoryOutput(success=True, error=None)
