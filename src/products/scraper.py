import argparse
import requests
import sys
from typing import Any, Dict
from src.products.base import Product


def prepare_product_url(ean_code: str) -> str:
    return f"https://world.openfoodfacts.org/api/v0/product/{ean_code}.json"


def download_product_data(ean_code: str) -> Dict[str, Any] | None:
    url = prepare_product_url(ean_code)
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f"Fetching data failed, reason: {exc}")
        return None
    product_data = response.json()
    if product_data["status"] != 1:
        print("Product not found")
        return None
    return product_data


def postprocess_product_data(product_data: Dict[str, Any]) -> Product:
    def _get_field(dictionary: Dict[str, Any], key: str) -> Any:
        return dictionary.get(key, None)

    def _convert_quantity_to_grams(quantity: str) -> float:
        if quantity.lower().endswith("kg") or (
            quantity.lower().endswith("l") and not quantity.lower().endswith("ml")
        ):
            quantity_g = float(quantity[:-2].strip()) * 1000
        elif quantity.endswith("g") or quantity.endswith("ml"):
            quantity_g = float(quantity[:-2].strip())
        else:
            quantity_g = 0
            print(f"Unknown quantity unit: {quantity}")
        return quantity_g

    def _get_quantity(product_data: Dict[str, Any]) -> float:
        quantity = _get_field(product_data["product"], "quantity")
        return _convert_quantity_to_grams(quantity)

    def _get_tags(product_data: Dict[str, Any]) -> str:
        tags = _get_field(product_data["product"], "categories_tags")
        return ", ".join([tag.split(":")[-1] for tag in tags])

    def _unpack_nutriments_data(product_data: Dict[str, Any]) -> Dict[str, Any]:
        valuable_keys = [
            "energy-kcal_100g",
            "carbohydrates_100g",
            "fat_100g",
            "proteins_100g",
            "fiber_100g",
            "salt_100g",
            "saturated-fat_100g",
            "sodium_100g",
            "sugars_100g",
        ]

        nutriments_data = {}
        if not (
            nutriments_raw_data := _get_field(product_data["product"], "nutriments")
        ):
            print("No nutriments data present")
            return nutriments_data

        for key in valuable_keys:
            if value := _get_field(nutriments_raw_data, key):
                nutriments_data[key.replace("-", "_")] = value
        return nutriments_data

    postprocessed_data = {}
    postprocessed_data["name"] = _get_field(product_data["product"], "product_name")
    postprocessed_data["brand"] = _get_field(product_data["product"], "brands")
    postprocessed_data["ean_code"] = _get_field(product_data, "code")
    postprocessed_data["quantity_g"] = _get_quantity(product_data)
    postprocessed_data["tags"] = _get_tags(product_data)
    postprocessed_data.update(_unpack_nutriments_data(product_data))
    return Product.from_dict(postprocessed_data)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fetch and process product data from Open Food Facts."
    )
    parser.add_argument("ean_code", help="The EAN code of the product to look up")
    return parser.parse_args()


def main() -> Dict[str, Any] | None:
    args = parse_arguments()
    product_data = download_product_data(args.ean_code)
    if product_data is None:
        print("Failed to retrieve product data.")
        return None

    processed_data = postprocess_product_data(product_data)

    return processed_data


if __name__ == "__main__":
    result = main()
    if result is None:
        sys.exit(1)
    print(result)
    sys.exit(0)
