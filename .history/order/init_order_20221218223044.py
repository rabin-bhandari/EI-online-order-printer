import json
from types import SimpleNamespace
from order_object import Order

f = open('../example_order.json')

order_json = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))


order = Order(order_json)

for item in order.order_items.values():
    print(str(item.quantity) +" - " + item.name + " - " + str(item.price))
