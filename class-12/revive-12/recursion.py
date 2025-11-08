def factorial(x):
    if x < 1:
        print('Invalid number')
        return 'Invalid number'
    if x == 1:
        return 1
    return x * factorial(x-1)

# f(n) = n * f(n-1)
print(factorial(6))
print(factorial(-1))
print(factorial(10))