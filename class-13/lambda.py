# lambda arguments: expression
squareLambda = lambda x: x**2
def square(x):
    return x**2

print(square(2))
print(squareLambda(2))

sumLambda = lambda x, y: x + y
def sum(x,y):
    return x+y

print(sum(12,65))
print(sumLambda(12,65))

lambda x, y, z: x*y*z
def product(x,y,z):
    return x*y*z

lambda x: x % 2 == 0
def is_even(x):
    return x % 2 == 0

lambda x: x % 2 != 0
def is_odd(x):
    return x % 2 != 0

lambda x: x * 2
def double(x):
    return x * 2

lambda x: x / 2
def half(x):
    return x / 2

to_uppercase_lambda = lambda s: s.upper()
def to_uppercase(s):
    return s.upper()

print(to_uppercase('miftah'))
print(to_uppercase_lambda('miftah'))

lambda s: len(s)
def string_length(s):
    return len(s)

lambda x, y: x > y
def is_greater(x, y):
    return x > y

lambda x, y: max(x, y)
def maximum(x, y):
    return max(x, y)

lambda x, y: min(x, y)
def minimum(x, y):
    return min(x, y)

lambda x: x if x > 0 else 0
def positive_or_zero(x):
    return x if x > 0 else 0

lambda x: "Even" if x % 2 == 0 else "Odd"
def even_or_odd(x):
    return "Even" if x % 2 == 0 else "Odd"

lambda x: x ** 3
def cube(x):
    return x ** 3

lambda x, y: x ** y
def power(x, y):
    return x ** y

lambda lst: sum(lst)
def sum_list(lst):
    return sum(lst)

lambda lst: len(lst)
def list_length(lst):
    return len(lst)

lambda s: s[::-1]
def reverse_string(s):
    return s[::-1]

lambda x, y: (x + y) / 2
def average(x, y):
    return (x + y) / 2

lambda x: abs(x)
def absolute_value(x):
    return abs(x)

lambda name: f"Hello, {name}!"
def greet(name):
    return f"Hello, {name}!"