import argparse
import requests
import sys
from typing import Any, Dict


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


def postprocess_product_data(product_data: Dict[str, Any]) -> Dict[str, Any]:
    def _get_field(dictionary: Dict[str, Any], key: str) -> Any:
        return dictionary.get(key, None)

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
    postprocessed_data.update(_unpack_nutriments_data(product_data))
    return postprocessed_data
