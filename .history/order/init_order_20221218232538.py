import json
from types import SimpleNamespace
from .order_object import Order


def get_order():
    f = open('../example_order.json')
    order_json = json.loads(
        f.read(), object_hook=lambda d: SimpleNamespace(**d))
    order = Order(order_json)

    for item in order.order_items.values():
        print(str(item.quantity) + " - " + item.name + " - " + str(item.price))

    return order
/Users/Rabin/Documents/EI-online-order-printer/example_order.json
/Users/Rabin/Documents/EI-online-order-printer/order/init_order.py