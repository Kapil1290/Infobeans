class BankAccount:
    def __init__(self, name, account_number, amount):
        self.__name = name
        self.__acc_num = account_number
        self.__amount = amount
    def withdrawing(self):
        pass

class saving_account(BankAccount):
    def __init__(self,name,account_number,amount):
        super().__init__(name,account_number, amount)
    def withdrawing(self):
        amt = float(input("Enter amount for withdraw: "))
        if self.__amount > amt:
            self.__amount -= amt

class current_account(BankAccount):
    def withdrawing(self):
        print("your can only withdraw 10,00000+/day")

s = saving_account()
s.withdrawing()