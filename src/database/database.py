import sqlite3
from typing import List, Tuple
from src.products.base import Product
from src.intake.base import Intake
from src.database.utils import temporary_chdir

DATABASE_NAME = "foodtrack_TESTS.db"  # TODO: Move to config


def create_tables():
    create_products_table()
    create_intake_table()


@temporary_chdir("src/database")
def create_products_table():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                ean_code TEXT PRIMARY KEY,
                name TEXT,
                brand TEXT,
                tags TEXT,
                quantity_g REAL,
                energy_kcal_100g REAL,
                carbohydrates_100g REAL,
                fat_100g REAL,
                proteins_100g REAL,
                fiber_100g REAL,
                salt_100g REAL,
                saturated_fat_100g REAL,
                sodium_100g REAL,
                sugars_100g REAL
            )
            """
        )
        conn.commit()


@temporary_chdir("src/database")
def create_intake_table():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS intake (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ean_code TEXT,
                name TEXT,
                quantity_g REAL,
                datetime TEXT,
                meal_type TEXT,
                energy_kcal REAL,
                carbohydrates_g REAL,
                fats_g REAL,
                proteins_g REAL,
                fiber_g REAL,
                salt_g REAL,
                saturated_fat_g REAL,
                sodium_g REAL,
                sugars_g REAL,
                FOREIGN KEY(ean_code) REFERENCES products(ean_code)
            )
            """
        )
        conn.commit()


@temporary_chdir("src/database")
def insert_product(product: Product):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO products (
                ean_code, name, brand, tags, quantity_g, energy_kcal_100g, carbohydrates_100g, fat_100g, proteins_100g, fiber_100g, salt_100g, saturated_fat_100g, sodium_100g, sugars_100g
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                product.ean_code,
                product.name,
                product.brand,
                product.tags,
                product.quantity_g,
                product.energy_kcal_100g,
                product.carbohydrates_100g,
                product.fat_100g,
                product.proteins_100g,
                product.fiber_100g,
                product.salt_100g,
                product.saturated_fat_100g,
                product.sodium_100g,
                product.sugars_100g,
            ),
        )
        conn.commit()


@temporary_chdir("src/database")
def insert_intake(intake: Intake):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO intake (
            ean_code, name, quantity_g, datetime, meal_type, energy_kcal, carbohydrates_g, fats_g, proteins_g, fiber_g, salt_g, saturated_fat_g, sodium_g, sugars_g
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                intake.ean_code,
                intake.name,
                intake.quantity_g,
                intake.intake_datetime,
                intake.meal_type,
                intake.energy_kcal,
                intake.carbohydrates_g,
                intake.fats_g,
                intake.proteins_g,
                intake.fiber_g,
                intake.salt_g,
                intake.saturated_fat_g,
                intake.sodium_g,
                intake.sugars_g,
            ),
        )
        conn.commit()


@temporary_chdir("src/database")
def get_product_by_ean(ean_code: str) -> Product:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM products WHERE ean_code = ?
            """,
            (ean_code,),
        )
        product_data = cursor.fetchone()
        if product_data is None:
            return None
        column_names = [description[0] for description in cursor.description]
        product_dict = dict(zip(column_names, product_data))
    return Product.from_dict(product_dict)


@temporary_chdir("src/database")
def get_list_of_all_products() -> List[Tuple[str, str]]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT ean_code, name, brand FROM products
            """
        )
        products_data = cursor.fetchall()
        if products_data is None:
            return []
        products = [(ean_code, f"{name} ({brand})") for ean_code, name, brand in products_data]
    return products


@temporary_chdir("src/database")
def remove_product_by_ean(ean_code: str):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM products WHERE ean_code = ?
            """,
            (ean_code,),
        )
        conn.commit()