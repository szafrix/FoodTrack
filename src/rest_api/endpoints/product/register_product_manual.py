from fastapi import Depends
from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
    RegisterProductInRepositoryUseCaseInput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide

class RegisterProductManualInputRequest(BaseModel):
    name: str
    kcal_100g: float
    proteins_100g: float
    carbs_100g: float
    fats_100g: float


class RegisterProductManualInputResponse(BaseModel):
    product: Product

async def register_product_manual_input(
    request: RegisterProductManualInputRequest,
    register_product_use_case: RegisterProductInRepositoryUseCase = Depends(
        Provide[Container.register_product_in_repository_use_case]
    ),
) -> RegisterProductManualInputResponse:
    product = Product(
        name=request.name,
        kcal_100g=request.kcal_100g,
        proteins_100g=request.proteins_100g,
        carbs_100g=request.carbs_100g,
        fats_100g=request.fats_100g,
    )
    use_case_input = RegisterProductInRepositoryUseCaseInput(
        product=product,
    )
    use_case_output = register_product_use_case.execute(use_case_input)
    return RegisterProductManualInputResponse(
        product=use_case_output.product,
    )
