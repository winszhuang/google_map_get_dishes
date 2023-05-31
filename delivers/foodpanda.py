import requests
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
                image = ""
                if len(product["images"]) > 0:
                    image = product["images"][0]["image_url"]
                price = ""
                if len(product["product_variations"]) > 0:
                    price = product["product_variations"][0]["price"]
                dish = Dish(name, description, image, price, category_name)
                dishes.append(dish)
        return dishes
    except Exception as e:
        print("fetch dishes error")
        print(e)
        return []


def get_dishes(restaurant_page_url: str) -> list[Dish]:
    # url like https://www.foodpanda.com.tw/restaurant/u0gl/ming-zhi-gao-xian-xian-chao-guan?utm_source=google&utm_medium=organic&utm_campaign=google_reserve_place_order_action
    restaurant_id = get_id_by_url(restaurant_page_url)

    return fetch_dishes(restaurant_id)


def get_id_by_url(url: str):
    return url.split("restaurant/")[1].split("/")[0]
