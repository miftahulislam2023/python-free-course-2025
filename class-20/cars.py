# class Car:
#     brand = ''
#     model = ''

# car1 = Car()
# car1.brand = 'BMW'
# car1.model = 'OSW'

class Car:
    def __init__(s, brand, model, price):
        s.brand = brand
        s.model = model
        s.price = price

# car1 = Car('BMW', 'OJK', 21000)
# print(car1.price)
# print(car1.model)
# print(car1.brand)

cars = [
    Car('BMW', 'OJK', 21000),
    Car('AS', 'ADF', 9000),
    Car('KKS', 'OSK', 1000),
    Car('RA', 'M4', 50000),
    Car('JK', 'RI', 200000),
]

for car in cars:
    print(car.brand)
    print(car.model)
    print(car.price)