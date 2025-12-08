class Customer:
    def __init__(self, id, budget):
        self.id = id
        self.budget = budget
    
    def buyProduct(self, price):
        self.budget -= price #budget = budget - price

    def applyCoupon(self, code):
        pass

c1 = Customer('23', 5000)
print(c1.budget)
c1.buyProduct(3000)
print(c1.budget)
c1.buyProduct(1000)
print(c1.budget)
c1.buyProduct(500)
print(c1.budget)

c2 = Customer('50', 10000)
print(c2.budget)
c2.buyProduct(3000)
print(c2.budget)
c2.buyProduct(1000)
print(c2.budget)
c2.buyProduct(500)
print(c2.budget)