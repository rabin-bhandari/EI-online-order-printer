from types import SimpleNamespace
from escpos import *
import os
import zpl
from printer_config import Printer
# INITIALISE PRINTERS
LABEL_PRINTER = printer.Network(Printer.LABEL.value)
KITCHEN_PRINTER = printer.Network(Printer.KITCHEN.value)
BILL_PRINTER = printer.Network(Printer.BILL.value)

from printer_drivers.label_printer import print_labels
from order.init_order import get_order




# INITIALISE ORDER
order = get_order()

def print_order(order):   
    # PRINT BAR RECEIPT


    # PRINT CHEF'S RECEIPT


    # PRINT LABELS
    print_labels(order.name, order.number, order.order_items)
    print("adfasdfasdf")

print_order(order)