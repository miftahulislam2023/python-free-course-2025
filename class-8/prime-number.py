x = int(input('Enter a number:'))
isPrime = True #flag variable
i = 2
while i < x:
    if x % i == 0:
        isPrime = False
        break
    i+=1

if isPrime:
    print('Prime')
else:
    print('Not prime')