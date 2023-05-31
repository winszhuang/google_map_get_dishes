from model.dish import Dish

import delivers.foodpanda as foodpanda
import delivers.ubereats as ubereats

strategy = {"ubereats": ubereats.get_dishes, "foodpanda": foodpanda.get_dishes}


def check_deliver(url: str):
    if url.find("ubereats.com") != -1: return "ubereats"
    if url.find("foodpanda.com") != -1: return "foodpanda"
    return ""


def get_dishes(restaurant_page_url: str) -> list[Dish]:
    deliver_name = check_deliver(restaurant_page_url)
    if deliver_name == "":
        raise Exception("No deliver")
    value = strategy.get(deliver_name)
    if value is None:
        raise Exception("No such deliver")

    return strategy[deliver_name](restaurant_page_url)
