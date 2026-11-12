class Library:
    total_books = 0
    book_collection = []
    def __init__(self, id, title, author, available_status=True):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__available_status = available_status
        Library.total_books+=1
        
        # to_add = {"id":id, "title": title, "author": author, "available_status":available_status}
        Library.book_collection.append({"id":id, "title": title, "author": author, "available_status":available_status})
        print(Library.book_collection)
    
    def issue_book(self, id):
        for i in range(0, len(Library.book_collection)):
            if Library.book_collection[i]['id'] == id and Library.book_collection[i]['available_status'] == True:
                Library.book_collection[i]['available_status'] = False
                print("Book Issued")
                break
        else:
            print("Book not available......")
    
    def return_book(self, id):
        for i in range(0, len(Library.book_collection)):
            if Library.book_collection[i]['id'] == id and Library.book_collection[i]['available_status'] == False:
                Library.book_collection[i]['available_status'] = True
                print("Book returned")
                break
        else:
            print("Invalid Book id......")

    def available_books(self):
         print([book for book in Library.book_collection if book['available_status']==True])

l1 = Library(101, "R D P D", "Robert")
l1.issue_book(101)
l1.return_book(101)
l1.available_books()
