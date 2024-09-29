from src.adapters.repositories.product_repository import IIntakeRepository
from src.core.entities.requests.fetch_product_requests import RegisterIntakeRequest


class RegisterIntake:
    def __init__(self, intake_repository: IIntakeRepository):
        self.intake_repository = intake_repository

    def execute(self, register_intake_request: RegisterIntakeRequest) -> None:
        self.intake_repository.register_intake(register_intake_request)
