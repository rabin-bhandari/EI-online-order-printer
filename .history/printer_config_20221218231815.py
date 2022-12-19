from enum import Enum
from escpos

class Printer(Enum):
    KITCHEN = "192.168.1.193"
    BILL = "192.168.1.194"
    LABEL = "192.168.1.195"