while True:
    celcius = float(input('Enter temperature:'))
    if celcius < -273:
        print("Invalid temperature. Exiting....")
        break
    farenheit = celcius * 9 / 5 + 32
    print(farenheit)