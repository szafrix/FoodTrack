from abc import ABC, abstractmethod
from src.core.repositories.intake.models import (
    SaveIntakeToRepositoryInput,
    SaveIntakeToRepositoryOutput,
    GetIntakesByDateRepositoryInput,
    GetIntakesByDateRepositoryOutput,
)


class IntakeRepository(ABC):

    @abstractmethod
    def save_intake(
        self, input_: SaveIntakeToRepositoryInput
    ) -> SaveIntakeToRepositoryOutput:
        pass

    @abstractmethod
    def get_intakes_by_date(
        self, input_: GetIntakesByDateRepositoryInput
    ) -> GetIntakesByDateRepositoryOutput:
        pass
