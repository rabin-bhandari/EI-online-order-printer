import os
import zpl

name = "Rabin Bhandari"
number = "07908044186"
customerDetails = name + " | " + number

item = "Chicken Chilli Masala"

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


print(l.dumpZPL())
# l.preview()
