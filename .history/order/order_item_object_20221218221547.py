
class OrderItem:
    def __init__(self, itemDetails):
        self.name = itemDetails.item_name + " "+ itemDetails.variety_name
        self.quantity = int(itemDetails.qty)
        self.price = "{:.2f}".format(float(itemDetails.total)
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, OrderItem):
            return self.name == other.name
        return False