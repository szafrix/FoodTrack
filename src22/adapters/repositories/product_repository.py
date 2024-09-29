import sqlite3
from typing import List, Optional, Union

from src.core.entities.product import Product
from src.core.entities.requests.fetch_product_requests import (
    FetchProductByBarcodeRequest, FetchProductByNameRequest)


class IProductRepository:
    def register_product(self, product: Product) -> None:
        pass

    def fetch_product(
        self, request: Union[FetchProductByBarcodeRequest, FetchProductByNameRequest]
    ) -> Optional[Product]:
        pass


class SQLiteProductRepository(IProductRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def register_product(self, product: Product) -> None:
        pass

    def fetch_product(
        self, request: Union[FetchProductByBarcodeRequest, FetchProductByNameRequest]
    ) -> Optional[Product]:
        pass
