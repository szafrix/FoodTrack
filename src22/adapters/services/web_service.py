from typing import Optional
from abc import ABC, abstractmethod


class WebServiceInput:
    def __init__(self, barcode: str):
        self.barcode = barcode


class WebServiceOutput:
    def __init__(self, barcode: str):
        self.barcode = barcode


class IWebService(ABC):
    @abstractmethod
    def scrape_product_from_web(
        self, input_: WebServiceInput
    ) -> Optional[WebServiceOutput]:
        pass


class OpenFoodFactsWebService(IWebService):
    def scrape_product_from_web(
        self, input_: WebServiceInput
    ) -> Optional[WebServiceOutput]:
        pass
