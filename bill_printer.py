# from tkinter import CENTER
from escpos import *
import datetime

# p = printer.Network("10.1.2.192")
p = printer.Network("192.168.1.194")


DIVIDER = "------------------------------------------"
DIVIDER_V2 = "=========================================="

CONTACTS = "Mersham Le Hatch\n" + "The Courtyard\n" + "Ashford\n" + \
    "Kent\n" + "TN25 6NH\n" + "Tel:01233-557557\n" + "Vat: 337 1390 77\n\n\n"


def header(printer, string):
    printer.set(font="a", height=2, width=2, align="center", text_type="b")
    printer.text(string)
    printer.text("\n\n")
    printer.set(align="center")
    printer.text(CONTACTS)


def align(printer, left, right, left_s, right_s):
    sizing = "{:<"+str(left_s)+"}{:>"+str(right_s)+"}"
    printer.text(sizing.format(left, right))
    # printer.text("{:<20}{:>21}".format(left, right))
    printer.text("\n")


def dateTime(printer):
    time = "Time: "+datetime.datetime.now().strftime("%H:%M")
    date = "Date: "+datetime.date.today().strftime("%d/%m/%y")
    printer.set(align="left")
    align(printer, date, time, 20, 21)
    printer.text(DIVIDER)
    printer.text("\n\n\n\n\n\n\n")


def order(printer):
    printer.set(font="a", height=2, width=2, align="center", text_type="a")
    printer.text("ORDER CONTENT")
    printer.text("\n\n\n\n\n\n")
    printer.set()
    printer.text(DIVIDER_V2)


def total(printer, amount):

    printer.set(font="a", height=2, width=1, align="center", text_type="b")
    align(printer, "Total:", str(amount), 20, 21)
    printer.set()
    printer.text(DIVIDER_V2)


def customerDetails(printer, name, address, number):
    printer.set(font="a", height=2, width=1,
                align="center")
    name = "Customer: " + name
    align(printer, name, number, 20, 21)
    printer.block_text(address, 20)
    printer.text("\n")
    printer.set()
    printer.text(DIVIDER_V2)
    printer.text("\n\n\n\n")


# DUMMY
TITLE = "ONLINE ORDER"
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
