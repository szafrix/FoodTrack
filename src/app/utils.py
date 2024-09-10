from src.products.scraper import download_product_data, postprocess_product_data
from src.database.database import (
    insert_product,
    get_product_by_ean,
    get_list_of_all_products,
)
from src.intake.base import Intake
from src.intake.utils import record_intake
from src.products.base import Product
import streamlit as st


def fetch_product(ean_code: str) -> Product | None:
    if product_instance := get_product_by_ean(ean_code):
        return product_instance
    elif product_data := download_product_data(ean_code):
        product_instance = postprocess_product_data(product_data)
        return product_instance
    else:
        return None


def manual_product_input() -> Product | None:
    st.subheader("Manual Product Input")
    name = st.text_input("Product Name")
    brand = st.text_input("Brand")
    tags = st.text_input("Tags")
    quantity_g = st.number_input("Quantity (g)", min_value=0.0)
    energy_kcal_100g = st.number_input("Energy (kcal/100g)", min_value=0.0)
    carbohydrates_100g = st.number_input("Carbohydrates (g/100g)", min_value=0.0)
    fat_100g = st.number_input("Fat (g/100g)", min_value=0.0)
    proteins_100g = st.number_input("Proteins (g/100g)", min_value=0.0)
    fiber_100g = st.number_input("Fiber (g/100g)", min_value=0.0)
    salt_100g = st.number_input("Salt (g/100g)", min_value=0.0)
    saturated_fat_100g = st.number_input("Saturated Fat (g/100g)", min_value=0.0)
    sodium_100g = st.number_input("Sodium (g/100g)", min_value=0.0)
    sugars_100g = st.number_input("Sugars (g/100g)", min_value=0.0)

    # Add more fields as needed

    if st.button("Save Product"):
        new_product = Product(
            name=name,
            ean_code=st.session_state.ean_code,
            brand=brand,
            tags=tags,
            quantity_g=quantity_g,
            energy_kcal_100g=energy_kcal_100g,
            carbohydrates_100g=carbohydrates_100g,
            fat_100g=fat_100g,
            proteins_100g=proteins_100g,
            fiber_100g=fiber_100g,
            salt_100g=salt_100g,
            saturated_fat_100g=saturated_fat_100g,
            sodium_100g=sodium_100g,
            sugars_100g=sugars_100g,
        )
        insert_product(new_product)
        st.success("Product saved successfully!")
        return new_product
    return None


def reset_app():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
