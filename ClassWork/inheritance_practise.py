class Area:
    def __init__(self, l, w):
        self.__l = l
        self.__w = w

    def calc_area(self):
        return self.__l*self.__w
    
class Volume(Area): 
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.__h = h

    def get_volume(self):
        return self.calc_area() * self.__h

class Density(Volume):
    def __init__(self,l,w,h,m):
       super().__init__(l,w,h)
       self.__m = m

    def calc_density(self):
        return self.get_volume() // self.__m

a = Density(1,2,3,4)
print(a.calc_density())
