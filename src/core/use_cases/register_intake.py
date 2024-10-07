from pydantic import BaseModel
from src.core.entities.product import Product
from datetime import datetime
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.intake.models import SaveIntakeToRepositoryInput
from src.core.exceptions import BaseError, UnexpectedError

logger = getLogger(__name__)


class RegisterIntakeUseCaseInput(BaseModel):
    product: Product
    quantity: int
    date: datetime


class RegisterIntakeUseCaseOutput(BaseModel):
    success: bool
    message: str


class RegisterIntakeUseCase:
    def __init__(self, intake_repository: IntakeRepository):
        self.intake_repository = intake_repository

    def register_intake(
        self, input_: RegisterIntakeUseCaseInput
    ) -> RegisterIntakeUseCaseOutput:
        try:
            save_intake_to_repository_input = SaveIntakeToRepositoryInput(
                product=input_.product,
                quantity=input_.quantity,
                date=input_.date,
            )
            save_intake_to_repository_output = self.intake_repository.save_intake(
                save_intake_to_repository_input
            )
            return save_intake_to_repository_output
        except BaseError as exc:
            logger.error(f"Error while registering intake {exc}", exc_info=True)
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while registering intake {exc}",
                exc_info=True,
            )
