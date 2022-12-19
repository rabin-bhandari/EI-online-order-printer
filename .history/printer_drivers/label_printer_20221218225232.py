# from tkinter import CENTER
from escpos import *
import os
import zpl
from 

#  kitchen label printer -> 192.168.1.195
# p = printer.Network("192.168.1.195")


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


def print_labels(name, number, items):
    for item in items:
        raw = label_content(name, number, item)
        printer._raw(raw.encode)

