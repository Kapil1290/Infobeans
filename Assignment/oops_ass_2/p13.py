class Exam:
    __total_exam = 0
    def __init__(self,name,total_mark,pass_mark):
        self.__name = name
        self.__total = total_mark
        self.__pass = pass_mark

    def check_result(self,obtain_mark):
        if obtain_mark>=self.__pass and obtain_mark<=100:
            print("Pass")
        else:
            print("Fail")

    @staticmethod
    def check_grade(percentage):
        if 90<=percentage<=100:
            print("Grade A")
        elif 75<=percentage<90:
            print("Grade B")
        elif 55<=percentage<75:
            print("Grade C")
        elif 45<=percentage<55:
            print("Grade D")
        else:
            print("E Very Poor or Fail")
        
    def get_grade(self, percent):
        Exam.check_grade(percent)

    @classmethod
    def get_total_exam(cls):
        print(cls.__total_exam)

e1 = Exam("python",100,58)
e1.check_result(58)
e1.get_grade(78)