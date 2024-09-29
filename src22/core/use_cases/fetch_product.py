from typing import Optional, Union

from src.adapters.repositories.product_repository import IProductRepository
from src.core.entities.product import Product
from src.core.entities.requests.fetch_product_requests import (
    FetchProductByBarcodeRequest,
    FetchProductByNameRequest,
)
from src.core.exceptions import BarcodeNotFoundError, ProductNotFoundError
from src.adapters.services.barcode_service import IBarcodeService
from src.adapters.services.web_service import IWebService


class FetchProduct:
    def __init__(
        self,
        product_repository: IProductRepository,
        web_service: IWebService,
        barcode_service: IBarcodeService,
    ):
        self.product_repository = product_repository
        self.web_service = web_service
        self.barcode_service = barcode_service

    def execute(
        self,
        fetch_product_request: Union[
            FetchProductByBarcodeRequest, FetchProductByNameRequest
        ],
    ) -> Optional[Product]:
        if isinstance(fetch_product_request, FetchProductByBarcodeRequest):
            return self._fetch_product_by_barcode(fetch_product_request)
        elif isinstance(fetch_product_request, FetchProductByNameRequest):
            return self._fetch_product_by_name(fetch_product_request)

    def _fetch_product_by_barcode(
        self, fetch_product_request: FetchProductByBarcodeRequest
    ) -> Product:
        try:
            barcode = self.barcode_service.decode_barcode(fetch_product_request)
        except BarcodeNotFoundError:
            raise BarcodeNotFoundError

        if product := self._fetch_product_by_barcode_from_repository(barcode):
            return product

        if product := self._scrape_product_from_web(barcode):
            return product

        raise ProductNotFoundError

    def _fetch_product_by_barcode_from_repository(
        self, barcode: str
    ) -> Optional[Product]:
        return self.product_repository.fetch_product_by_barcode(barcode)

    def _scrape_product_from_web(self, barcode: str) -> Optional[Product]:
        return self.web_service.get_product_by_barcode(barcode)
