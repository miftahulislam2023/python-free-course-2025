def square (x):
    print(x**2)

def celciusToFarenheit(celcius):
    farenheit = celcius * 9 / 5 + 32
    print(farenheit)

def namota(x):
    tenX = x * 10
    temp = x
    while x <= tenX:
        print(x)
        x += temp

square(12)
square(3)
celciusToFarenheit(22)
square(7)
namota(12)
celciusToFarenheit(34)
namota(19)
namota(7)
namota(23)