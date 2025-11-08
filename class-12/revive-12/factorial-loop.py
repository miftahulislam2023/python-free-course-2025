def factorialUsingLoop(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    print(result)

factorialUsingLoop(5)
factorialUsingLoop(6)
factorialUsingLoop(7)
factorialUsingLoop(4)
