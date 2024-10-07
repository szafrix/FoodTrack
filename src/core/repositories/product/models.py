from pydantic import BaseModel
from src.core.entities.product import Product


class SearchProductsForAutocompletionInput(BaseModel):
    query: str


class SearchProductsForAutocompletionOutput(BaseModel):
    products: list[Product]


class SaveProductToRepositoryInput(BaseModel):
    product: Product


class SaveProductToRepositoryOutput(BaseModel):
    product: Product
