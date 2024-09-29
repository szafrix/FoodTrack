from abc import ABC, abstractmethod
from src.core.entities.product import Product
from pydantic import BaseModel

class GetProductFromRepositoryInput(BaseModel):
    product_name: str


class GetProductFromRepositoryOutput(BaseModel):
    success: bool
    product: Product | None
    error: str | None


class SaveProductToRepositoryInput(BaseModel):
    product: Product


class SaveProductToRepositoryOutput(BaseModel):
    success: bool
    error: str | None


class ProductRepository(ABC):
    @abstractmethod
    def get_product(self, input_: GetProductFromRepositoryInput) -> GetProductFromRepositoryOutput:
        pass

    @abstractmethod
    def save_product(self, input_: SaveProductToRepositoryInput) -> SaveProductToRepositoryOutput:
        pass
