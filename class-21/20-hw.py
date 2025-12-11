class Customer:
    coupons = {
        'DEC': 20,
        'LAST': 30,
        'NG': 40
    }

    def __init__(self, id, budget, coupon):
        self.id = id
        self.budget = budget
        self.coupon = coupon

    def buyProduct(self, price):
        couponValue = 0
        for key, value in self.coupons.items():
            if key == self.coupon:
                couponValue = value
        discountedPrice = price * (100-couponValue) / 100
        self.budget = self.budget - discountedPrice

c1 = Customer(2, 5000, 'NG')
c1.buyProduct(1000)
print(c1.budget)

c2 = Customer(8, 10000, 'DEC')
c2.buyProduct(1000)
print(c2.budget)