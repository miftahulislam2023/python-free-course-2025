class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       
        self.__balance = balance
        self.__balance2 = balance
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, newBalance):
        self.__balance = newBalance

    def getBalance2(self):
        return self.__balance2
    
    def setBalance2(self, newBalance):
        self.__balance2 = newBalance
    

aiblAccount = BankAccount('Miftahul Islam', 10000)
print(aiblAccount.getBalance())
aiblAccount.setBalance(14000)
print(aiblAccount.getBalance())
print(aiblAccount.__balance)
aiblAccount.__balance = 15000
print(aiblAccount.__balance2)
# print(aiblAccount.__balance)