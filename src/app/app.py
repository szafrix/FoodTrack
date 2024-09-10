import streamlit as st
from src.database.database import get_list_of_all_products
from src.app.utils import fetch_product, manual_product_input, reset_app
from src.intake.utils import record_intake
from datetime import datetime
from time import sleep

DATABASE_PRODUCTS = get_list_of_all_products()

def main():
    st.title("Record food intake")

    if st.button("Reset App"):
        reset_app()
        st.rerun()

    if "product" not in st.session_state:
        st.session_state.product = None
    if "ean_code" not in st.session_state:
        st.session_state.ean_code = None
    if "show_manual_input" not in st.session_state:
        st.session_state.show_manual_input = False

    ean_input_method = st.radio(
        "Choose EAN input method:", ["Select from list", "Enter custom EAN"]
    )

    if ean_input_method == "Select from list":
        if selected_ean := st.selectbox(
            "Select a product:",
            options=DATABASE_PRODUCTS,
            format_func=lambda x: f"{x[1]} ({x[0]})",
        ):
            st.session_state.ean_code = selected_ean[0]
    else:
        st.session_state.ean_code = st.text_input("Enter custom EAN code:")

    if st.button("Fetch product data"):
        product = fetch_product(st.session_state.ean_code)
        if product:
            st.session_state.product = product
        else:
            st.write("Product not found. Please input the product manually.")
            st.session_state.show_manual_input = True

    if st.session_state.show_manual_input:
        st.session_state.product = manual_product_input()

    if st.session_state.product:
        st.session_state.show_manual_input = False
        st.write(st.session_state.product.print_detailed_info_in_tabular_format())

        st.subheader("Record Intake")
        quantity = st.number_input(
            "Enter quantity consumed (g):", min_value=0.0, step=0.1
        )
        meal_type = st.selectbox(
            "Select meal type:", ["Breakfast", "Lunch", "Dinner", "Snack"]
        )
        intake_date = st.date_input("Date of intake", datetime.now())
        intake_time = st.time_input("Time of intake", datetime.now().time())

        if st.button("Record Intake"):
            intake_datetime = datetime.combine(intake_date, intake_time).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            record_intake(
                st.session_state.product, quantity, meal_type, intake_datetime
            )
            st.success("Intake recorded successfully!")
            sleep(5)
            st.session_state.product = None


if __name__ == "__main__":
    main()
