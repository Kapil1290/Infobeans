class Book:
    def __init__(self, id, title):
        self.__id = id
        self.__title = title
        self.__status = True

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"{self.__id} | {self.__title} | {self.__status}"
        

    def change_status(self, res):
        self.__status = res

class Library:
    __total_books = {}
    def add_book(self, id, title):
        Library.__total_books[id] = Book(id, title)

    def issue_book(self, id):
        if id not in Library.__total_books:
            print("Book not available")
            return
        if Library.__total_books[id].get_status():
            print("book issued")
            Library.__total_books[id].change_status(False)
        else:
            print("Book already issued ...")
    
    def return_book(self, id):
        if id in Library.__total_books:
            Library.__total_books[id].change_status(True)
            print("book returned...")

    def book_count(self):
        return len(Library.__total_books)
    
    def check_available(self):
        for book in Library.__total_books.values():
            if book.get_status():
                print(book)


l1 = Library()
l1.add_book(101, "the lesson")
l1.add_book(102, "the commit")
l1.issue_book(101)
# l1.return_book(101)
l1.issue_book(101)
l1.check_available()
print(l1.book_count())

class Movie:
    def __init__(name, ts):
        ts = ts
        name = nDepartment
        booked = 0

class MBS:
    __movies = {}

    