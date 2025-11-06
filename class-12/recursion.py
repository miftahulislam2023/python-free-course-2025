def factorial(n):
    n = int(n)
    if n < 1:
        print('Invalid number')
        return
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(4))
print(factorial(4))
print(factorial(-12))
print(factorial(10.34))