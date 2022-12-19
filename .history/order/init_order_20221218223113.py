import json
from types import SimpleNamespace
from order_object import Order



def get_order:
    

order = Order(order_json)

for item in order.order_items.values():
    print(str(item.quantity) +" - " + item.name + " - " + str(item.price))
