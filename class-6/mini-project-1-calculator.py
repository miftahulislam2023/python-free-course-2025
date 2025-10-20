try:
    x = float(input('Enter a number: '))
    y = float(input('Enter another number: '))
    operator = input('Enter an operator(+ - * /): ')
    if operator == '+':
        print(x + y)
    elif operator == '-':
        print(x - y)
    elif operator == '*':
        print(x * y)
    elif operator == '/':
        if(y == 0):
            print('Divisor can not be zero.')
        else:
            print(x / y)
    else:
        print('Invalid operator')
except ValueError:
    print('Error! Enter a number. Not other things.')