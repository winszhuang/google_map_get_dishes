import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from model.dish import Dish

# https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9hN2UxN2ZhMS1jY2IyLTQ2MDktYTZmYy03ZDI0MWRiMzczMjQuanBlZw==


def get_dishes(restaurant_page_url: str) -> list[Dish]:
    try:
        r = requests.get(restaurant_page_url)
        soup = BeautifulSoup(r.text, "html.parser")

        content = soup.find(id="main-content").find("script")
        json_data = json.loads(content.text)
        categories = json_data["hasMenu"]["hasMenuSection"]

        dishes = []
        for category in categories:
            category_name = category["name"]
            for dish in category["hasMenuItem"]:
                name = dish["name"]
                description = dish["description"]
                price = dish["offers"]["price"]
                dish = Dish(name, description, "", price, category_name)
                dishes.append(dish)
        return dishes

    except Exception as e:
        print("get dishes error")
        print(e)
        return []
