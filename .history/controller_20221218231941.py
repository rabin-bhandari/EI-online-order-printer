from order.init_order import get_order
from printer_drivers.label_printer import print_labels
from types import SimpleNamespace
from escpos import *
import os
import zpl



# INITIALISE ORDER
order = get_order()


def print_order(order):
    # PRINT BAR RECEIPT

    # PRINT CHEF'S RECEIPT

    # PRINT LABELS
    print_labels(order.name, order.number, order.order_items)
    print("adfasdfasdfa")


print_order(order)
