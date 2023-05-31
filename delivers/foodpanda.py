import requests
from urllib.parse import urlparse, parse_qs
import json
from model.dish import Dish

api_url = "https://tw.fd-api.com/api/v5/vendors/{restaurant_id}?include=menus,bundles,multiple_discounts&language_id=6&opening_type=delivery&basket_currency=TWD&show_pro_deals=true"


def fetch_dishes(restaurant_id):
    try:
        url = api_url.format(restaurant_id=restaurant_id)
        source = requests.get(url).json()
        categories = source["data"]["menus"][0]["menu_categories"]

        dishes = []
        for category in categories:
            category_name = category["name"]
            for product in category["products"]:
                name = product["name"]
                description = product["description"]
                image = product["images"][0]["image_url"]
                price = product["product_variations"][0]["price"]
                dish = Dish(name, description, image, price, category_name)
                dishes.append(dish)
        return dishes
    except Exception as e:
        print(e)
        return []


def get_dishes(restaurant_page_url: str) -> list[Dish]:
    start_index = restaurant_page_url.find("/restaurant/") + len(
        "/restaurant/")

    end_index = restaurant_page_url.find("/", start_index)
    restaurant_id = restaurant_page_url[start_index:end_index]

    return fetch_dishes(restaurant_id)
