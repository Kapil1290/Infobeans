class CricketPlayer:
    __total_players = 0
    def __init__(self, name, role, runs_scored=0):
        self.__name = name
        self.__role = role
        self.__run = runs_scored
        CricketPlayer.__total_players+=1

    def update_run(self, runs):
        self.__run = runs
        print("Run updated......")

    def __str__(self):
        return f"Name: {self.__name}\nRole: {self.__role}\nRunScored: {self.__run}\n"

    @classmethod
    def total_players(cls):
        print(f"Total players are: {cls.__total_players}")

    def statistics(self):
        print(self)


c1 = CricketPlayer("Kohli", "Batman", 70)
c1.update_run(90)
c1.statistics()