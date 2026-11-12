class Movie1:
    def __init__(self, title, director, *actors):
        self.__title = title
        self.__actor = list(actors)
        self.__director = director
        self.__review = []

    def add_review(self, *review):
        self.__review.extend(review)
        print(f"Review added.....review: {review}")
    
    def remove_review(self):
        self.__review.pop()
        print(f"review removed.....review: {self.__review}")

m1 = Movie1("rebel", "kunika", "amitabh", "sahruk","sunil")
# m1.add_review(4,2,3,5,4)
# m1.remove_review()