from abc import ABC, abstractmethod
from typing import Optional


class BarcodeServiceInput:
    def __init__(self, barcode: str):
        self.barcode = barcode


class BarcodeServiceOutput:
    def __init__(self, barcode: str):
        self.barcode = barcode


class IBarcodeService(ABC):
    @abstractmethod
    def decode_barcode(
        self, input_: BarcodeServiceInput
    ) -> Optional[BarcodeServiceOutput]:
        pass


class PyzbarBarcodeService(IBarcodeService):
    def decode_barcode(
        self, input_: BarcodeServiceInput
    ) -> Optional[BarcodeServiceOutput]:
        pass
