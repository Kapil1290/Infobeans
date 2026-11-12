class Bank:
    account_lib = []
    def add_account(self,account_detail):
        Bank.account_lib.append(account_detail)

    def remove(self, accNo):
        for i in range(0, len(Bank.account_lib)):
            if Bank.obj_lib[i]["_Account__accountNum"]==accNo:
                Bank.obj_lib.pop(i)
                break
        else:
            print(f"No acc found")
    def get_record(self):
        print(Bank.account_lib)



class Account:
    def __init__(self, name, age, account_number, account_type):
        self.__name = name
        self.__age = age
        self.__amount = 0
        self.__account_number = account_number
        self.__account_type = account_type

    def deposit(self, amt):
        self.__amount += amt
        print(f"Amount successfully deposited {self.__amount}")  

    def withdraw(self, amt):
        if self.__amount>=amt:
            self.__amount -= amt
            print(f"Amount successfully withdraw: {amt}")
        else:
            print(f"No sufficient amount.....")
    
    def get_details(self):
        dic = {
            "name": self.__name, "age":self.__age, "amount":self.__amount, "account_number":self.__account_number, "type":self.__account_type
        }
        return dic

a1 = Account("Kapil", 23, "2339847555", "saving")
a2 = Account("om", 22, "284995768", "current")
# a1.deposit(23000)
# a2.deposit(2000)  
# detail_saving = a1.get_details()
# detail_current = a2.get_details()
# a2.withdraw(23000)

# saving = Bank()
# current = Bank()
# current.add_account(detail_current)
# saving.add_account(detail_saving)
# current.get_record()