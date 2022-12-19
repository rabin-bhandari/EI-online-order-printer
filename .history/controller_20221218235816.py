from order.init_order import get_order
from printer_drivers.label_printer import print_labels



# INITIALISE ORDER
order = get_order()


def print_order(order):
    # PRINT BAR RECEIPT

    # PRINT CHEF'S RECEIPT
    

    # PRINT LABELS (DONE)
    # print_labels(order.name, order.number, order.order_items)


print_order(order)
