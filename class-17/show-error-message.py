try:
    x = int(input('Enter a number: '))
    print(10/x)
    print(10 + 'Str')
except Exception as e:
    print(e)
    print('Something went wrong!')
else:
    print('Everything is fine')
finally:
    print('I will always run!!!!')