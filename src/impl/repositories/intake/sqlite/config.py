from dataclasses import dataclass


@dataclass
class SQLiteIntakeRepositoryConfig:
    db_path: str = "data/intake.db"
