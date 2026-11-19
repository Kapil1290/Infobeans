
class Library:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id 

    def borrow(self):
        pass

    def getborrowed(self):
        pass

class Book(Library):
    __book_collection = {}
    def __init__(self, name, id, author):
        super().__init__(name,id)
        self.__author = author
        self.__borrowed_status = False
        Book.__book_collection[id] = {"id": id, "name":name, "author":author}
    
    def borrow(self, id):
        if not self.__borrowed_status and id in Book.__book_collection:
            print("Book borrowed....")
        else:
            print("Book already borrowed")

    def returned(self, id):
        if self.__borrowed_status and id in Book.__book_collection:
            print("Book returned....")
            self.__borrowed_status = False
        else:
            if id not in Book.__book_collection:
                print("No id available")
            else:
                print("already borrowed")

class Magazine(Library):
    __magazine_collection = {}
    def __init__(self, name, id):
        super().__init__(name,id)
        self.__borrowed_status = False
        Magazine.__magazine_collection[id]={"name":name,"id":id}

    def borrow(self,id):
        if not self.__borrowed_status and id in Magazine.__magazine_collection:
            print("Book borrowed....")
            self.__borrowed_status = True
        else:
            print("magazinee already borrowed")

    def returned(self, id):
        if self.__borrowed_status and id in Magazine.__magazine_collection:
            print("magazine returned....")
            self.__borrowed_status = False
        else:
            if id not in Magazine.__magazine_collection:
                print("No id available")
            else:
                print("already borrowed")


class Newspaper(Library): 
    __newspaper_collection = {}
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__borrowed_status = False
        Newspaper.__newspaper_collection[id]={"name":name,"id":id}

    def borrow(self):
        if not self.__borrowed_status and id not in Newspaper.__newspaper_collection:
            print("newspaper borrowed....")
            self.__borrowed_status = True
        else:
            print("newspaper already borrowed")

    def returned(self, id):
        if  self.__borrowed_status and id in Newspaper.__newspaper_collection:
            print("newspaper returned....")
            self.__borrowed_status = False
        else:
            if id not in Newspaper.__newspaper_collection:
                print("No id available")
            else:
                print("already borrowed")
    

n = Newspaper("patrika",1)
n.borrow()
n.returned(1)
