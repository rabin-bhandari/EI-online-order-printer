# from tkinter import CENTER
from escpos import *
import datetime
from ..printer_config import KITCHEN_PRINTER
# p = printer.Network("10.1.2.192")
# p = printer.Network("192.168.1.193")


DIVIDER = "------------------------------------------\n"
DIVIDER_V2 = "==========================================\n"

def print_kitchen_reciept(order):
    title = order.order_type.upper()  
    header(KITCHEN_PRINTER, title)

def header(printer, title):
    printer.text(DIVIDER_V2)
    printer.set(font="a", height=2, width=2, align="center", text_type="b")
    printer.text(title)
    printer.text("\n")
    printer.set(align="center")
    printer.text(DIVIDER_V2)


def align(printer, left, right, left_s, right_s):
    sizing = "{:<"+str(left_s)+"}{:>"+str(right_s)+"}"
    printer.text(sizing.format(left, right))
    printer.text("\n")


def dateTime(printer):
    time = "Time: "+datetime.datetime.now().strftime("%H:%M")
    date = "Date: "+datetime.date.today().strftime("%d/%m/%y")
    printer.set(font="a", height=3, width=1, align="left", text_type="b")
    align(printer, date, time, 20, 21)
    printer.set()
    printer.text(DIVIDER)
    printer.text("\n\n\n\n\n\n")


def order(printer):
    printer.set(font="a", height=2, width=2, align="center", text_type="a")
    printer.text("ORDER CONTENT")
    printer.text("\n\n\n\n\n\n")
    printer.set()
    printer.text("Item Total: 0")
    printer.text("\n")
    printer.text(DIVIDER_V2)


def total(printer, amount):

    printer.set(font="a", height=2, width=1, align="center", text_type="b")
    align(printer, "Total:", str(amount), 20, 21)
    printer.set()
    printer.text(DIVIDER_V2)


def customerDetails(printer, name, address, number):
    printer.set(font="a", height=2, width=1,
                align="left")
    name = "Customer: " + name
    align(printer, name, number, 20, 21)
    printer.text(address)
    printer.text("\n")
    printer.set()
    printer.text(DIVIDER_V2)
    printer.text("\n\n\n\n")


# DUMMY
TITLE = "COLLECTION ORDER"
TOTAL = 123.45

NAME = "Ravi"
ADDRESS = "254 Broadwalk,\nLondon,\nSE38NQ"
NUMBER = "07908044186"

header(p, TITLE)
dateTime(p)
order(p)
total(p, TOTAL)
customerDetails(p, NAME,
                ADDRESS, NUMBER)


p.set()
p.cut()
p.control("LF")
p.control("LF")
