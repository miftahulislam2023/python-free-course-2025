class Book:
    def __init__(self, title, author, price, code):
        self.title = title
        self.author = author
        self.price = price
        self.__code = code
    
    def getCode(self):
        return self.__code
    
    def setCode(self, newcode):
        self.__code = newcode

book1 = Book('Theory of Relativity', 'Miftahul Islam', 200, 'ABC321')
# print(book1.__code)
print(book1.getCode())
print(book1.setCode('EFG343'))
print(book1.getCode())