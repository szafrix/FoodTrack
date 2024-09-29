from fastapi import APIRouter, Depends
from ..models.product import (
    RegisterProductByNameRequest,
    RegisterProductByBarcodeRequest,
    RegisterProductByNameResponse,
    RegisterProductByBarcodeResponse,
)
from src.core.use_cases.register_product_by_name import (
    RegisterProductByName,
    RegisterProductByNameInput,
)
from src.core.use_cases.register_product_by_barcode import (
    RegisterProductByBarcode,
    RegisterProductByBarcodeInput,
)

router = APIRouter()


@router.post("/product/register/by-name", response_model=RegisterProductByNameResponse)
async def register_product_by_name(
    request: RegisterProductByNameRequest, use_case: RegisterProductByName = Depends()
):
    use_case_input = RegisterProductByNameInput.from_request(request)
    result = use_case.execute(use_case_input)
    return RegisterProductByNameResponse.from_use_case_response(result)


@router.post(
    "/product/register/by-barcode", response_model=RegisterProductByBarcodeResponse
)
async def register_product_by_barcode(
    request: RegisterProductByBarcodeRequest,
    use_case: RegisterProductByBarcode = Depends(),
):
    use_case_input = RegisterProductByBarcodeInput(barcode=request.barcode)
    result = use_case.execute(use_case_input)
    return RegisterProductByBarcodeResponse.from_use_case_response(result)
