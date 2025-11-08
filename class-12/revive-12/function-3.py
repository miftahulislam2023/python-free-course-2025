def namota():
    x = int(input('Enter a number: '))
    tenX = x * 10
    temp = x
    while x <= tenX:
        print(x)
        x += temp

namota()