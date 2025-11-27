try:
    x = int(input('Enter a number: '))
    print(10/x)
except:
    print('Something went wrong!')
else:
    print('Everything is fine')
finally:
    print('I will always run!!!!')