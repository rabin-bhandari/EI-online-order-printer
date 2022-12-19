from enum import Enum
from escpos import *

class Printer(Enum):
    KITCHEN = "192.168.1.193"
    BILL = "192.168.1.194"
    LABEL = "192.168.1.195"


# INITIALISE PRINTERS
LABEL_PRINTER = printer.Network(Printer.LABEL.value)
KITCHEN_PRINTER = printer.Network(Printer.KITCHEN.value)
BILL_PRINTER = printer.Network(Printer.BILL.value)