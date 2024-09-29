from pydantic import BaseModel
from src.core.use_cases.register_intake_by_name import RegisterIntakeOutput


class RegisterIntakeRequest(BaseModel):
    product_name: str
    quantity: float
    meal_type: str
    date: str


class RegisterIntakeResponse(BaseModel):
    intake_id: int
    product_name: str
    quantity: float
    meal_type: str
    date: str

    @classmethod
    def from_use_case_response(cls, use_case_response: RegisterIntakeOutput):
        return cls(
            intake_id=use_case_response.intake_id,
            product_name=use_case_response.product_name,
            quantity=use_case_response.quantity,
            meal_type=use_case_response.meal_type,
            date=use_case_response.date,
        )
