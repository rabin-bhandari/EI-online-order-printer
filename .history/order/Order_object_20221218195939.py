
# Superclass

class Order:
    def __init__(self, name, number, order_type, order_items, is_Paid, is_Prerorder, preorder_date, preorder_time, discount_code, discount_amount, notes, delivery_address,):
        self.name = name
        self.number = number
        self.order_type = order_type
        self.order_items = order_items
        self.is_Paid = is_Paid
        self.is_Prerorder = is_Prerorder
        self.preorder_date = preorder_date
        self.preorder_time = preorder_time
        self.discount_code = discount_code
        self.discount_amount = discount_amount
        self.notes = notes
        self.delivery_address = delivery_address
        

order = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))
