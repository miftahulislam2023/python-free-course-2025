class Father:
    def gift(self):
        print("father's gift")

class Mother:
    def gift(self):
        print("mother's gift")

class Child(Mother, Father): 
    def gift(self):
        print('child"s gift')
    # pass

c = Child()
c.gift()