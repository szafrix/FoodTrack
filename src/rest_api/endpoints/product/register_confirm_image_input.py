from pydantic import BaseModel
from fastapi import Depends
from src.core.entities.product import Product
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
    RegisterProductInRepositoryUseCaseInput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide


class RegisterConfirmImageInputInput(BaseModel):
    product: Product


class RegisterConfirmImageInputResponse(BaseModel):
    product: Product


async def confirm_product_image_input(
    product: Product,
    register_product_use_case: RegisterProductInRepositoryUseCase = Depends(
        Provide[Container.register_product_in_repository_use_case]
    ),
) -> RegisterConfirmImageInputResponse:
    register_product_use_case_input = RegisterProductInRepositoryUseCaseInput(
        product=product,
    )
    register_product_use_case_output = register_product_use_case.execute(
        register_product_use_case_input
    )
    return RegisterConfirmImageInputResponse(
        product=register_product_use_case_output.product,
    )
