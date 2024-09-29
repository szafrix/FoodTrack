# send test request

import requests
import json


url = "http://localhost:8000/register_product_manual_input/try_to_fetch"

data = {
    "name": "Test Product",
    "kcal_100g": 100,
    "proteins_100g": 10,
    "carbs_100g": 10,
    "fats_100g": 10,
}

response = requests.post(
    url, data=json.dumps(data), headers={"Content-Type": "application/json"}
)

print(response.json())

url = "http://localhost:8000/register_product_manual_input/do_not_fetch"

data = {
    "name": "Test Product",
    "kcal_100g": 100,
    "proteins_100g": 10,
    "carbs_100g": 10,
    "fats_100g": 10,
}

response = requests.post(
    url, data=json.dumps(data), headers={"Content-Type": "application/json"}
)

print(response.json())

url = "http://localhost:8000/register_product_image_input/try_to_fetch"

data = {
    "name": "Test Product",
    "nutrients_image": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
}

response = requests.post(
    url, data=json.dumps(data), headers={"Content-Type": "application/json"}
)

print(response.json())

url = "http://localhost:8000/register_product_image_input/do_not_fetch"

data = {
    "name": "Test Product",
    "nutrients_image": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
}

response = requests.post(
    url, data=json.dumps(data), headers={"Content-Type": "application/json"}
)

print(response.json())
