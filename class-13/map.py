n = [i for i in range(1, 21)]
print(n)
nSquare = [i**2 for i in range(1,21)] # using list comprehension
print(nSquare)

def square(x):
    return x**2

print(list(map(lambda x: x**2, n))) # using map
print(list(map(square, n))) # using map

