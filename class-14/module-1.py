# full import
import math_functions
print(math_functions.square(2))

# full import with rename
import math_functions as m
print(m.square(2))

# partial import - আংশিক ইম্পোর্ট
from math_functions import square
print(square(45))