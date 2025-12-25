class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        if self.y < 0:
            print(f'{self.x}{self.y}i')
        else:
            print(f'{self.x}+{self.y}i')
    
    def __add__(self, other):
        return Complex(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Complex(self.x-other.x, self.y-other.y)
    
    def __str__(self):
        if self.y < 0:
            return(f'{self.x}{self.y}i')
        else:
            return(f'{self.x}+{self.y}i')

c1 = Complex(12, 7)
c1.print()
c2 = Complex(3, -5)
c2.print()
c3 = c1 + c2
c3.print()
c4 = c1 - c2
c4.print()

print(c1)


