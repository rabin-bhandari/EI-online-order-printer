from types import SimpleNamespace
from escpos import *
import os
import zpl
from printer_drivers.label_printer import print_labels
from order.init_order import get_order
from 

# INITIALISE PRINTERS
label_printer = printer.Network(Printer.LABEL.value)

# INITIALISE ORDER
order = get_order()

# PRINT BAR RECEIPT


# PRINT CHEF'S RECEIPT


# PRINT LABELS


