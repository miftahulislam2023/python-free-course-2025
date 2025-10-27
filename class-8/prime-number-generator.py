max = int(input('Enter the max value:'))
x = 3
while x <= max:
    isPrime = True #flag variable
    i = 2
    while i < x/2:
        if x % i == 0:
            isPrime = False
            break
        i+=1

    if isPrime:
        print(x)
    x+=1