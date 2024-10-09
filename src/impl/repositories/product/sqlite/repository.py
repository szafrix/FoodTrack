from src.core.repositories.product.repository import ProductRepository
from src.core.repositories.product.models import (
    SearchProductsForAutocompletionInput,
    SearchProductsForAutocompletionOutput,
    SaveProductToRepositoryInput,
    SaveProductToRepositoryOutput,
    GetProductsRepositoryInput,
    GetProductsRepositoryOutput,
)
from src.core.entities.product import Product
import sqlite3
import os
from src.impl.repositories.product.sqlite.config import SQLiteProductRepositoryConfig
from src.core.repositories.product.exceptions import (
    ProductRepositoryError,
    SearchProductsForAutocompletionError,
    SaveProductError,
    GetProductsError,
)


class SQLiteProductRepository(ProductRepository):
    def __init__(self, config: SQLiteProductRepositoryConfig):
        self.db_path = config.db_path
        self._create_table()

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                        CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            kcal_100g REAL NOT NULL,
                            proteins_100g REAL NOT NULL,
                            carbs_100g REAL NOT NULL,
                            fats_100g REAL NOT NULL
                        )
                    """
                )
                conn.commit()
        except Exception as exc:
            raise ProductRepositoryError(f"Error creating products table") from exc

    def search_products_for_autocompletion(
        self, input_: SearchProductsForAutocompletionInput
    ) -> SearchProductsForAutocompletionOutput:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM products WHERE LOWER(name) LIKE LOWER(?) LIMIT 10",
                    (f"%{input_.query}%",),
                )
                results = cursor.fetchall()

            products = [
                Product(
                    id_=row[0],
                    name=row[1],
                    kcal_100g=row[2],
                    proteins_100g=row[3],
                    carbs_100g=row[4],
                    fats_100g=row[5],
                )
                for row in results
            ]

            return SearchProductsForAutocompletionOutput(products=products)
        except Exception as exc:
            raise SearchProductsForAutocompletionError(
                f"Error searching products for autocompletion"
            ) from exc

    def save_product(
        self, input_: SaveProductToRepositoryInput
    ) -> SaveProductToRepositoryOutput:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                if input_.product.id_ is None:
                    cursor.execute(
                        """
                        INSERT INTO products (name, kcal_100g, proteins_100g, carbs_100g, fats_100g)
                        VALUES (?, ?, ?, ?, ?)
                    """,
                        (
                            input_.product.name,
                            input_.product.kcal_100g,
                            input_.product.proteins_100g,
                            input_.product.carbs_100g,
                            input_.product.fats_100g,
                        ),
                    )
                    input_.product.id_ = cursor.lastrowid
                else:
                    cursor.execute(
                        """
                        UPDATE products
                        SET name = ?, kcal_100g = ?, proteins_100g = ?, carbs_100g = ?, fats_100g = ?
                        WHERE id = ?
                    """,
                        (
                            input_.product.name,
                            input_.product.kcal_100g,
                            input_.product.proteins_100g,
                            input_.product.carbs_100g,
                            input_.product.fats_100g,
                            input_.product.id_,
                        ),
                    )
                conn.commit()

            return SaveProductToRepositoryOutput(product=input_.product)
        except Exception as exc:
            raise SaveProductError(f"Error saving product") from exc

    def get_products(
        self, input_: GetProductsRepositoryInput
    ) -> GetProductsRepositoryOutput:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM products WHERE id IN (?)", (input_.product_ids,)
                )
                results = cursor.fetchall()

            products = [
                Product(
                    id_=row[0],
                    name=row[1],
                    kcal_100g=row[2],
                    proteins_100g=row[3],
                    carbs_100g=row[4],
                    fats_100g=row[5],
                )
                for row in results
            ]

            return GetProductsRepositoryOutput(products=products)
        except Exception as exc:
            raise GetProductsError(f"Error getting products") from exc
