from typing import List
import sqlite3

from src.core.entities.intake import Intake
from typing import Union, Optional
from src.core.entities.requests.fetch_product_requests import RegisterIntakeRequest


class IIntakeRepository:
    def register_intake(self, intake: Intake) -> None:
        pass


class SQLiteIntakeRepository(IIntakeRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def register_product(self, intake: Intake) -> None:
        pass

    def fetch_product(self, request: Union[RegisterIntakeRequest]) -> Optional[Intake]:
        pass
