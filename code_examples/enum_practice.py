from enum import Enum

class Color(Enum):
   RED = 1
   GREEN = 2
   BLUE = 3
   
print("BLUE == 3 ", Color.BLUE == 3)
print("BLUE is 3 ", Color.BLUE is 3)
print("BLUE.value == 3", Color.BLUE.value == 3)

from enum import Enum, auto

class Role(Enum):
    DOG = auto()
    CAT = auto()
    BID = auto()
    
print ("CAT ", Role.CAT)    
print("is CAT == 2 ", Role.CAT == 2)

print("CAT == GREEN ", Color.GREEN == Role.CAT)

from enum import IntEnum

class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2

class Request(IntEnum):
    POST = 1
    GET = 2
    
    
print("CIRCLE == 1 ", Shape.CIRCLE == 1) 

print("CIRCLE = POST ", Shape.CIRCLE == Request.POST)   