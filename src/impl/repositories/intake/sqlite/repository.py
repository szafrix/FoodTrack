from logging import getLogger
from src.core.entities.intake import Intake
from src.core.repositories.intake.repository import IntakeRepository
from src.core.repositories.intake.models import (
    SaveIntakeToRepositoryInput,
    SaveIntakeToRepositoryOutput,
    GetIntakesByDateRepositoryInput,
    GetIntakesByDateRepositoryOutput,
)
import sqlite3
from src.impl.repositories.intake.sqlite.config import SQLiteIntakeRepositoryConfig
from src.core.repositories.intake.exceptions import (
    IntakeRepositoryError,
    SaveIntakeError,
    GetIntakesByDateError,
)

logger = getLogger(__name__)


class SQLiteIntakeRepository(IntakeRepository):
    def __init__(self, config: SQLiteIntakeRepositoryConfig):
        self.db_path = config.db_path
        self._create_table()

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS intakes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id INTEGER NOT NULL,
                        product_name TEXT NOT NULL,
                        quantity_g INTEGER NOT NULL,
                        date TIMESTAMP NOT NULL,
                        FOREIGN KEY (product_id) REFERENCES products (id)
                    )
                """
                )
                conn.commit()
        except Exception as exc:
            raise IntakeRepositoryError(f"Error creating intakes table") from exc

    def save_intake(
        self, input_: SaveIntakeToRepositoryInput
    ) -> SaveIntakeToRepositoryOutput:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                INSERT INTO intakes (product_id, product_name, quantity_g, date)
                VALUES (?, ?, ?, ?)
            """,
                    (
                        input_.product.id_,
                        input_.product.name,
                        input_.quantity,
                        input_.date.isoformat(),
                    ),
                )
            conn.commit()
            last_row_id = cursor.lastrowid

            return SaveIntakeToRepositoryOutput(
                success=True, message="Intake saved successfully", intake_id=last_row_id
            )
        except Exception as exc:
            raise SaveIntakeError(f"Error saving intake") from exc

    def get_intakes_by_date(
        self, input_: GetIntakesByDateRepositoryInput
    ) -> GetIntakesByDateRepositoryOutput:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM intakes WHERE date = ?", (input_.date,))
                results = cursor.fetchall()

            intakes = [
                Intake(
                    product_name=row[2],
                    quantity_g=row[3],
                    date=row[4],
                )
                for row in results
            ]

            return GetIntakesByDateRepositoryOutput(intakes=intakes)
        except Exception as exc:
            raise GetIntakesByDateError(f"Error getting intakes by date") from exc
