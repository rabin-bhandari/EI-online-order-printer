from types import SimpleNamespace
from escpos import *
import os
import zpl
from printer_drivers.label_printer import print_labels

label_printer = printer.Network("192.168.1.195")
bill_printer = printer.Network("192.168.1.194")
kitchen_printer = printer.Network("192.168.1.193")



# PRINT BAR RECEIPT


# PRINT CHEF'S RECEIPT


# PRINT LABELS

print_labels(label_printer, name, number, order_items)

def order_items_helper(orderItems):
    # think about multiple 
    dict ={}
    for item in orderItems:
        item_name = item.get(item_name)+item.get(variety_name)
        dict[item_name] = dict.get(item_name,0)+item.get(total)
    return dict