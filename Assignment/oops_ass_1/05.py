

class Book1:
    def __init__(self):
        self.__collection = []
    

    def add(self, title, author, isbn):
        self.__title= title
        self.__author = author
        self.__isbn = isbn
        self.__collection.append({"title":self.__title,"author":self.__author,"isbn":self.__isbn})

    def remove(self, isbn):
        for i in range(0, len(self.__collection)):
            if self.__collection[i]["isbn"]==isbn:
                self.__collection.pop(i)
                print(f"Book deleted with isbn: {isbn}")
                break
        else:
            print(f"Book not found with isbn: {isbn}")

    def current_collection(self):
        print(f"{self.__collection}")

b1 = Book1()
b1.add("The new aura", "john doe", 2132)
b1.add("Time is gold", "ratibi", 2354)
b1.add("Time is gold", "ratibi", 5255)
b1.add("The Real world", "micheal", 7658)
# b1.current_collection()
# b1.remove(7658)
# b1.current_collection()