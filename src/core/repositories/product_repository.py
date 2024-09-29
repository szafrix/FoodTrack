from abc import ABC, abstractmethod

from typing import List, Optional, Union

from src.core.entities.product import Product
from src.core.entities.requests.fetch_product_requests import (
    FetchProductByBarcodeRequest, FetchProductByNameRequest)


class IProductRepository(ABC):
    @abstractmethod
    def register_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def fetch_product(
        self, request: Union[FetchProductByBarcodeRequest, FetchProductByNameRequest]
    ) -> Optional[Product]:
        pass


