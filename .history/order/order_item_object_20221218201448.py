
class OrderItem:
    def __init__(self, itemDetails):
        self.name = itemDetails.item_name + itemDetails.variety_name
        self.quantity = itemDetails.qty
        self.price = itemDetails.price