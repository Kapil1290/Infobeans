class Airoplane:
    def __init__(self, flight_number, destination, depart_time):
        self.__flight_number = flight_number
        self.__destination = destination
        self.__depart_time = depart_time

    def check_status(self):
        print(f"Flight Details\nFlight Number: {self.__flight_number}\nDestination: {self.__destination}\nDepartTime: {self.__depart_time}")

a1 = Airoplane(233, "Hydrabad", "12:30 PM")
a2 = Airoplane(112, "London", "11:00 AM")
# a1.check_status()
# a2.check_status()