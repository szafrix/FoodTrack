import sqlite3
from typing import Optional, Union

from src.core.entities.intake import Intake
from src.repositories.intake_repository import IIntakeRepository
from src.core.entities.requests.fetch_product_requests import RegisterIntakeRequest
from src.repositories.intake_repository import (
    RegisterIntakeRepositoryRequest,
    RegisterIntakeRepositoryResponse,
)


class SQLiteIntakeRepository(IIntakeRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def register_intake(
        self, input_data: RegisterIntakeRepositoryRequest
    ) -> RegisterIntakeRepositoryResponse:
        pass

    def fetch_product(self, request: Union[RegisterIntakeRequest]) -> Optional[Intake]:
        pass
