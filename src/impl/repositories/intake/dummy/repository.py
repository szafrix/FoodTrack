from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.intake.models import (
    SaveIntakeToRepositoryInput,
    SaveIntakeToRepositoryOutput,
)


class DummyIntakeRepository(IntakeRepository):
    def save_intake(
        self, input_: SaveIntakeToRepositoryInput
    ) -> SaveIntakeToRepositoryOutput:
        print(
            f"Saving {input_.product.name} with quantity {input_.quantity} at {input_.date}"
        )
        return SaveIntakeToRepositoryOutput(success=True, message="Intake saved")
