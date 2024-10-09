from pydantic import BaseModel
from src.core.entities.product import Product


class GetProductsRepositoryInput(BaseModel):
    product_names: list[str]


class GetProductsRepositoryOutput(BaseModel):
    products: list[Product]


class SearchProductsForAutocompletionInput(BaseModel):
    query: str


class SearchProductsForAutocompletionOutput(BaseModel):
    products: list[Product]


class SaveProductToRepositoryInput(BaseModel):
    product: Product


class SaveProductToRepositoryOutput(BaseModel):
    product: Product
