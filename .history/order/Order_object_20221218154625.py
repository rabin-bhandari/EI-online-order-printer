class Order:
    def __init__(self, name, number, order_type, order_items, is_Paid,):
        pass


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