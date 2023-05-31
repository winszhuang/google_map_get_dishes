from model.dish import Dish
import ubereats
import foodpanda

strategy = {"ubereats": ubereats.get_dishes, "foodpanda": foodpanda.get_dishes}


def get_dishes(deliver_name: str, restaurant_page_url: str) -> list[Dish]:
    value = strategy.get(deliver_name)
    if value is None:
        raise Exception("No such deliver")

    return strategy[deliver_name](restaurant_page_url)
