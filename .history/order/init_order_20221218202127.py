import json
from types import SimpleNamespace
from order_object import Order

f = open('example_order.json')

order_json = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))

order = Order(order_json)

# Need order number

def collect_ordder_items()



# def order_items_helper(orderItems):
#     # think about multiple
#     dict = {}
#     for item in orderItems:
#         item_name = item.get(item_name)+item.get(variety_name)
#         dict[item_name] = dict.get(item_name, 0)+item.get(total)
#     return dict
