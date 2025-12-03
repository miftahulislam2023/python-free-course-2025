class Car:
    brand = ''
    title = ''
    price = 0
    edition = ''
    def horn():
        print('')

car1 = Car()
car1.brand = 'Toyota'
car1.title = 'Camry'
car1.price = 25000
car1.edition = '2020'

car2 = Car()
car2.brand = 'Honda'
car2.title = 'Civic'
car2.price = 22000
car2.edition = '2019'

car3 = Car()
car3.brand = 'Ford'
car3.title = 'Mustang'
car3.price = 35000
car3.edition = '2021'

print("Car 1:")
print(car1.brand)
print(car1.price)
print(car1.edition)
print(car1.title)

print("\nCar 2:")
print(car2.brand)
print(car2.price)
print(car2.edition)
print(car2.title)

print("\nCar 3:")
print(car3.brand)
print(car3.price)
print(car3.edition)
print(car3.title)