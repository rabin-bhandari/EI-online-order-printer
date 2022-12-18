import json
from types import SimpleNamespace
from order_object
f = open('example_order.json')

order = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))



name = order.name.title()
number = order.mobile
order_type = order.order_type.title()
order_items = order_items_helper(order.order_items)
is_Paid = order.payment_status.title()
is_Preorder = order.preorder
preorder_date = order.datetime
preorder_time = order.datetime

discount_code = order.discount_code
discount_amount = order.discount_amount

notes = order.notes

delivery_address = order.delivery_address

# Need order number





# def order_items_helper(orderItems):
#     # think about multiple
#     dict = {}
#     for item in orderItems:
#         item_name = item.get(item_name)+item.get(variety_name)
#         dict[item_name] = dict.get(item_name, 0)+item.get(total)
#     return dict
