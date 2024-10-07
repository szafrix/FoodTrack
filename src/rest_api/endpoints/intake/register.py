from fastapi import Depends
from pydantic import BaseModel
from src.core.entities.product import Product
from datetime import datetime
from src.core.use_cases.register_intake import (
    RegisterIntakeUseCase,
    RegisterIntakeUseCaseInput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide


class RegisterIntakeRequest(BaseModel):
    product: Product
    quantity: int
    date: datetime


class RegisterIntakeResponse(BaseModel):
    success: bool
    message: str


async def register_intake(
    request: RegisterIntakeRequest,
    register_intake_use_case: RegisterIntakeUseCase = Depends(
        Provide[Container.register_intake_use_case]
    ),
) -> RegisterIntakeResponse:
    use_case_input = RegisterIntakeUseCaseInput(
        product=request.product,
        quantity=request.quantity,
        date=request.date,
    )
    use_case_output = register_intake_use_case.register_intake(use_case_input)
    return RegisterIntakeResponse(
        success=use_case_output.success, message=use_case_output.message
    )
