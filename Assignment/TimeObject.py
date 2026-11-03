

class Time:

    def __init__(self, hrs, min, sec):
        self.__hrs = hrs
        self.__min = min
        self.__sec = sec
    
    def add_time(self, time_1_obj, time_2_obj):
        self.__hrs = time_1_obj.__hrs + time_2_obj.__hrs

        self.__min = time_1_obj.__min + time_2_obj.__min
        if self.__min>=60:
            self.__hrs += 1
            self.__min -= 60
        
        self.__sec = time_1_obj.__sec + time_2_obj.__sec

        while self.__sec>=60:
            self.__min += 1
            self.__sec -=60

        print(f"Added time is: {self.__hrs}Hr {self.__min}Min {self.__sec}Sec")

t1 = Time(1,20,121)
t2 = Time(2,70,120)

t3 = Time(0,0,0)

t3.add_time(t1, t2)