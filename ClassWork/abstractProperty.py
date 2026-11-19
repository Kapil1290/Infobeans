# from abc  import ABC, abstractmethod

# class A(ABC):
#     @property
#     @abstractmethod
#     def sound(self):
#         pass

# class B(A):
#     sound = "sounding"

# b = B()
# print(b.sound)



# print(B.mro())
# print(super(B,b))



class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    def show(self):
        print("C")
        super(C, self).show()

obj = C()
obj.show()