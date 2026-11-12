class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
    
    def set_breed(self, breed):
        self.__breed = breed

    def get_dog(self):
        print(f"DogName: {self.__name}\nBreed: {self.__breed}")
    
d1 = Dog("Puppy", "Labra")
d1.set_breed("Golden") # changing the breed
# d1.get_dog()