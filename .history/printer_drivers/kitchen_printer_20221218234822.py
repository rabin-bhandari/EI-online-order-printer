# from tkinter import CENTER
from escpos import *
import datetime
from ..printer_config import KITCHEN_PRINTER
# p = printer.Network("10.1.2.192")
# p = printer.Network("192.168.1.193")


DIVIDER = "------------------------------------------\n"
DIVIDER_V2 = "==========================================\n"

def print_kitchen_reciept(order):
    title = ("PRE-ORDER" if order.is_Preorder else '') + order.order_type.upper() 
    header(title)
    dateTime()
    order()
    total(order.total)
    customerDetails(p, NAME,
                    ADDRESS, NUMBER)

    
    KITCHEN_PRINTER.set()
    KITCHEN_PRINTER.cut()
    KITCHEN_PRINTER.control("LF")
    KITCHEN_PRINTER.control("LF")

def header( title):
    KITCHEN_PRINTER.text(DIVIDER_V2)
    KITCHEN_PRINTER.set(font="a", height=2, width=2, align="center", text_type="b")
    KITCHEN_PRINTER.text(title)
    KITCHEN_PRINTER.text("\n")
    KITCHEN_PRINTER.set(align="center")
    KITCHEN_PRINTER.text(DIVIDER_V2)


def align(left, right, left_s, right_s):
    sizing = "{:<"+str(left_s)+"}{:>"+str(right_s)+"}"
    KITCHEN_PRINTER.text(sizing.format(left, right))
    KITCHEN_PRINTER.text("\n")


def dateTime():
    time = "Time: "+datetime.datetime.now().strftime("%H:%M")
    date = "Date: "+datetime.date.today().strftime("%d/%m/%y")
    KITCHEN_PRINTER.set(font="a", height=3, width=1, align="left", text_type="b")
    align(KITCHEN_PRINTER, date, time, 20, 21)
    KITCHEN_PRINTER.set()
    KITCHEN_PRINTER.text(DIVIDER)
    KITCHEN_PRINTER.text("\n\n\n\n\n\n")


def order():
    KITCHEN_PRINTER.set(font="a", height=2, width=2, align="center", text_type="a")
    KITCHEN_PRINTER.text("ORDER CONTENT")
    KITCHEN_PRINTER.text("\n\n\n\n\n\n")
    KITCHEN_PRINTER.set()
    KITCHEN_PRINTER.text("Item Total: 0")
    KITCHEN_PRINTER.text("\n")
    KITCHEN_PRINTER.text(DIVIDER_V2)


def total(amount):

    KITCHEN_PRINTER.set(font="a", height=2, width=1, align="center", text_type="b")
    align(KITCHEN_PRINTER, "Total:", str(amount), 20, 21)
    KITCHEN_PRINTER.set()
    KITCHEN_PRINTER.text(DIVIDER_V2)


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




