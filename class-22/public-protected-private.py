class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public (সব জায়গায় এক্সেস করা যাবে)
        self._balance = balance  # Protected (বাইরে থেকে এক্সেস করা যাবে, তবে উচিত নয়)
        self.__balance = balance # Private (বাইরে থেকে এক্সেস করা যাবে না)

    def __privateMethod():
        pass
    
ibblAccount = BankAccount('Miftahul Islam', 5000)
print(ibblAccount.owner)
print(ibblAccount._balance)
print(ibblAccount.__balance)

ibblAccount._balance = 6000
print(ibblAccount._balance)
ibblAccount.__privateMethod()