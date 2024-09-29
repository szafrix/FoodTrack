from fastapi import APIRouter, Depends
from ..models.intake import RegisterIntakeRequest, RegisterIntakeResponse
from src.core.use_cases.register_intake_by_name import (
    RegisterIntake,
    RegisterIntakeInput,
)

router = APIRouter()


@router.post("/intake/register", response_model=RegisterIntakeResponse)
async def register_intake(
    request: RegisterIntakeRequest, use_case: RegisterIntake = Depends()
):
    use_case_input = RegisterIntakeInput(
        product_name=request.product_name,
        quantity=request.quantity,
        meal_type=request.meal_type,
        date=request.date,
    )
    result = use_case.execute(use_case_input)
    return RegisterIntakeResponse.from_use_case_response(result)
