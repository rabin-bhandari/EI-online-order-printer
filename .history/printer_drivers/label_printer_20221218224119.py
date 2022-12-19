# from tkinter import CENTER
from escpos import *
import os
import zpl
from printer_config import Printer


#  kitchen label printer -> 192.168.1.195
printer = printer.Network(Printer.LABEL.VALUE)



def label_content(name, number, item):
    customerDetails = name + " | " + number

    l = zpl.Label(25, 76)
    height = 5
    l.origin(10, height)
    l.write_text(customerDetails, char_height=3, char_width=3,
                line_width=76, justification='L')
    l.endorigin()
    height += 4
    l.origin(10, height)
    l.write_text(item, char_height=3, char_width=3,
                line_width=76, justification='L')
    l.endorigin()

    return l.dumpZPL()


def print_labels(printer, name, number, items):
    for item in items:
        raw = label_content(name, number, item, printer)
        printer._raw(raw.encode)


# p._raw(labelContent.encode())
