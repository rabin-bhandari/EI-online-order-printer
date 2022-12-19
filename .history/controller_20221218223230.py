from types import SimpleNamespace
from escpos import *
import os
import zpl
from printer_drivers.label_printer import print_labels
import get_order from order.init_order

label_printer = printer.Network("192.168.1.195")
bill_printer = printer.Network("192.168.1.194")
kitchen_printer = printer.Network("192.168.1.193")

order = get

# PRINT BAR RECEIPT


# PRINT CHEF'S RECEIPT


# PRINT LABELS

print_labels(label_printer, name, number, order_items)

