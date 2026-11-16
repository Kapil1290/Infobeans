class Train:
    def __init__(self,number, total_seat):
        self.__number = number
        self.__booked = 0
        self.__total = total_seat
    
    def get_total(self):
        return self.__total
    
    def set_total(self, total):
        self.__total -= total

    def inc_book(self):
        self.__booked += 1
        self.__total -= 1

    def dec_book(self):
        self.__booked -= 1
        self.__total += 1


class Booking:
    __booking = {}
    def add_train(self, number, total_seat):
        if number not in Booking.__booking:
            Booking.__booking[number] = Train( number, total_seat)
            print("train added")
            
        else:
            print("already added")

    def reservation(self, number):
        if number in Booking.__booking:
            Booking.__booking[number].inc_book()
        else:
            print("No train with this number....")

    def cancel(self, number):
        if number in Booking.__booking:
            Booking.__booking[number].dec_book()
        else:
            print("No train booked")

    def available_seats(self, number):
        print(f"Remaining seats: {Booking.__booking[number].get_total()}")


d1 = Booking()
d1.add_train(112, 4)
d1.reservation(112)
d1.reservation(112)
d1.cancel(112)
d1.available_seats(112)



    



