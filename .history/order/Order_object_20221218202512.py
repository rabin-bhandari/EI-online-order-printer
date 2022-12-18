from order_item_object import OrderItem
# Superclass

class Order:
    def __init__(self, order):
        self.name = order.name.title()
        self.number = order.mobile
        self.order_type = order.order_type.title()
        # self.order_items = order_items_helper(order.order_items)
        self.is_Paid = order.payment_status.title()
        self.is_Preorder = order.preorder
        self.preorder_date = order.datetime
        self.preorder_time = order.datetime
        self.discount_code = order.discount_code
        self.discount_amount = order.discount_amount
        self.notes = order.notes
        self.delivery_address = order.delivery_address
        
def collect_order_items(order_items):
    order_items_dict = {}
    for order_item in order_items:
        (
