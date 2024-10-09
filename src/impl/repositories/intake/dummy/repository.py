from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.intake.models import (
    SaveIntakeToRepositoryInput,
    SaveIntakeToRepositoryOutput,
    GetIntakesByDateRepositoryInput,
    GetIntakesByDateRepositoryOutput,
)
from src.core.entities.intake import Intake


class DummyIntakeRepository(IntakeRepository):
    def save_intake(
        self, input_: SaveIntakeToRepositoryInput
    ) -> SaveIntakeToRepositoryOutput:
        return SaveIntakeToRepositoryOutput(success=True, message="Intake saved")

    def get_intakes_by_date(
        self, input_: GetIntakesByDateRepositoryInput
    ) -> GetIntakesByDateRepositoryOutput:
        return GetIntakesByDateRepositoryOutput(
            intakes=[
                Intake(
                    product_name="Product 1",
                    quantity_g=1000,
                    date=input_.date,
                ),
                Intake(
                    product_name="Product 2",
                    quantity_g=2000,
                    date=input_.date,
                ),
            ]
        )
