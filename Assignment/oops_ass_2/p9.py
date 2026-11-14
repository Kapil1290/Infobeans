from datetime import datetime    

class ATM:
    __attemt = 3
    
    def __init__(self, name, balance, pin, number):
        self.__name = name
        self.__balance = balance
        self.__pin = pin
        self.__acc_num = number
        self.__status = False
        self.__statements = []
    

    def login_verify(self, pin):
        if ATM.__attemt>0:
            if pin==self.__pin:
                print("You logged in...")
                self.__status = True
            else:
                ATM.__attemt -= 1
                print(f"Invalid pin (attempt reamaining: {ATM.__attemt})")
        else:
            print("attempt finished!!!")
    
    def withdraw(self, amt):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.__status:
            if amt<=self.__balance:
                self.__balance -= amt
                self.__statements.append({
                    "Withdraw_amount": amt,
                    "Time": timestamp,
                    "Current_amount":self.__balance
                })
                print("amount withdrawed....")
            else:
                print("Insufficient balance.....")
        else:
            print("login first")

    def deposit(self, amt):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.__status:
            if amt>0:
                self.__balance += amt
                self.__statements.append({
                    "Deposit amount": amt,
                    "Time": timestamp,
                    "Current amount":self.__balance
                })
                print("amount deposited....")
            else:
                print("Negetive balance not applicable.....")
        else:
            print("login first")

    def change_pin(self, pin):
        if self.__status:
            if pin == 4:
                self.__pin = pin
                print("PIN changed...")
            else:
                print("invalid pin to set")
        else:
            print("login first")

    def mini_state(self):
        print("="*30)
        if self.__statements:
            for i in self.__statements:
                print(i)
        else:
            print("No any prior statements")

a1 = ATM("kapil", 10200, 1213, 9977979065)
a1.login_verify(1213)
a1.withdraw(5000)
a1.deposit(2000)
a1.mini_state()


    

