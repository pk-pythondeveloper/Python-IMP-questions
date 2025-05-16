#An Enum is a set of symbolic names bound to unique values
#They are most useful when you have a variable that can take one of a limited selection of values.
from enum import Enum,auto

class Weekday(Enum):
    MONDAY = 1
    # MONDAY=1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
#name keyword is used to print the value
# print(Weekday(10))s
print(type(Weekday(3)))
print(Weekday(1).name)
# print(Weekday(MONDAY)) #you cant passed 
print(Weekday.MONDAY.value) #its used get the values

# class Ordinal(AutoName):
#     NORTH = auto()
#     SOUTH = auto()
#     EAST = auto()
#     WEST = auto()
# Ordinal(ram)

from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print([member.name for member in Color])
print([member.value for member in Color])