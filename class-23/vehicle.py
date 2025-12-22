# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}-এর ইঞ্জিন চালু হয়েছে...")

# Child Class (Vehicle কে ইনহেরিট করছে)
class Car(Vehicle):
    def honk(self):
        print("পিপ পিপ!")

# অবজেক্ট তৈরি
my_car = Car("Toyota", "Corolla") # constructor use করলাম

# প্যারেন্ট ক্লাসের মেথড ব্যবহার
my_car.start_engine()  # আউটপুট: Toyota Corolla-এর ইঞ্জিন চালু হয়েছে...

# নিজের মেথড ব্যবহার
my_car.honk()          # আউটপুট: পিপ পিপ!