

#19
class Flight:
    def __init__(self, flight_id, destination, price):
        self.flight_id = flight_id
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"Flight Details: {self.flight_id}\nDestination: {self.destination}\nPrice: {self.price}"

    def __repr__(self):
        return self.__str__()

class Hotel:
    def __init__(self, hotel_id, name, price_per_night, city):
        self.hotel_id = hotel_id
        self.name = name
        self.price_per_night = price_per_night
        self.city = city

    def __str__(self):
        return f"Hotel Details: {self.hotel_id}\nCity: {self.city}\nPrice_per_day: {self.price_per_night}"

    def __repr__(self):
        return self.__str__()

class ReservationSystem:
    def __init__(self):
        self.flights = [
            Flight("B82", "Hydrabad", 10000),
            Flight("A23", "Mumbai", 50000),
            Flight("S32", "Delhi", 20000),
            Flight("V33", "Pune", 20000)
        ]
        self.hotels = [
            Hotel("BH12","Raja bhoj", 1200, "Jaipur"),
            Hotel("BA52","Yaswantji hotel", 5000, "Pune"),
            Hotel("BD42","Raja bhoj", 2500, "Mumbai")
        ]
        self.bookings = {}

    def search_flight(self, destination):
        return [f for f in self.flights if f.destination.lower() == destination.lower()]

    def search_hotel(self, city):
        return [ h for h in self.hotels if h.city.lower() == city.lower()]
    

    def book_flight(self, flight_id):
        for f in self.flights:
            if f.flight_id.lower() == flight_id.lower():
                print(f"FLIGHT SUCCESSFULLY BOOKED.")
                self.bookings[flight_id] = f
                break
        else:
            print(f"Flight not found.....")


    def book_hotel(self, hotel_id):
        for h in self.hotels:
            if h.hotel_id.lower() == hotel_id.lower():
                print(f"FLIGHT SUCCESSFULLY BOOKED.")
                self.bookings[hotel_id] = h
                break
        else:
            print(f"Hotel not found.....")

res = ReservationSystem()
data = res.search_flight("Pune")
# print(res.search_hotel("Pune"))

# res.book_flight("33")
# res.book_hotel("dfdf")
# print(data)
