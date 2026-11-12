class Library:
    def setter_details(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def display_detail(self):
        return self.__dict__
b1 = Book()
b1.setter_details("The last lesson", "Arvind Jaiswal", 450)
# print(b1.display_detail())