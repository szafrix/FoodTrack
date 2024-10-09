from src.core.exceptions import BaseError


class IntakeRepositoryError(BaseError):
    pass


class SaveIntakeError(IntakeRepositoryError):
    pass


class GetIntakesByDateError(IntakeRepositoryError):
    pass
