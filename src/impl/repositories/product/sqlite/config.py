from dataclasses import dataclass


@dataclass
class SQLiteProductRepositoryConfig:
    db_path: str = "data/product.db"
