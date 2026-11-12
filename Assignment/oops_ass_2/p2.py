class BankAccount:
    interest_rate = 12
    minimum_balance = 200.0
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    

    def withdraw(self, amt):
        if self.__balance <= amt:
            self.__balance -= amt
            print(f"Amount Withdrawed...")
        else:
            print(f"Insufficient Balance...")
        
    def deposit(self, amt):
        self.__balance += amt
        print(f"Amount Deposited...")

    def get_account_status(self):
        print(f"Holder: {self.__holder_name}\nAvailable Balance: {self.__balance}")
        return f"{self.__balance}"

    @staticmethod
    def validate_min_balance(balance):
        return balance >= BankAccount.minimum_balance

b1 = BankAccount("89746210037", "kapil", 100)
amt = b1.get_account_status()
print(b1.validate_min_balance(int(amt)))