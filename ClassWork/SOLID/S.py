# for BankFoundation all other class are abstracted 
class BankFoundation(ABC):
    @abstractmethod
    def payment(self):
        pass

class NetBanking(BankFoundation):
    def payment(self): 
        print("Payment done via net banking")

class UPI(BankFoundation):
    def payment(self):
        print("payment done via upi")

class CC(BankFoundation):             # if i want to develop new feature then it is good habit to implement it independently
    def payment(self):
        print()

upi = UPI()
upi.payment()