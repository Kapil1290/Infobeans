class Movie:
    def __init__(self, name, available_seat):
        self.__name = name
        self.__booked_seat = 0
        self.__available_seat = available_seat

    def get_available(self):
        return self.__available_seat
    
    def set_available(self):
        self.__available_seat -= 1
    
    def increase_available(self):
        self.__available_seat += 1
    
    def get_booked(self):
        return self.__booked_seat
    
    def set_booked(self):
        self.__booked_seat += 1
    
    def decrease_booked(self):
        self.__booked_seat -= 1

class BMS:
    __movies = {}
    def add_movie(self, name, total_seat):
        BMS.__movies[name] = Movie(name, total_seat)
        print("Movie added.....")
        return

    def book_ticket(self, name):
        if name not in BMS.__movies:
            print('movie not present')
            return
        if BMS.__movies[name].get_available() != 0:
            BMS.__movies[name].set_booked()
            print("Ticket booked..")
            BMS.__movies[name].set_available()
        else:
            print("Housefull........")

    def cancel_ticket(self, name):
        if BMS.__movies[name].get_booked()>0:
            BMS.__movies[name].decrease_booked()
            BMS.__movies[name].increase_available()
            print("Ticket cancelled......")
        else:
            print("Ticket not booked yet")

    def check_avail(self, name):
        print(f"Total tickets left: {BMS.__movies[name].get_available()}")
        return


movie = BMS()
movie.add_movie("Avengers",2)
movie.book_ticket("Avengers")
movie.cancel_ticket("Avengers")
movie.check_avail("Avengers")
