
class OrderItem:
    def __init__(self, itemDetails):
        self.name = itemDetails.item_name + itemDetails.variety_name
        self.quantity = itemDetails.qty
        self.price = itemDetails.total
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, CustomObject):
            return self.name == other.name and self.value == other.value
        return False