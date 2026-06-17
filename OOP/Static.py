#Static
class Student:

    @staticmethod
    def greet():
        print("Hello students")


Student.greet()

#Abstraction
class Car:
    def start(self):
        print("Car is starting...")

c = Car()
c.start()

#Encapsulation
class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        print("Marks:", self.__marks)


s1 = Student()

s1.set_marks(95)
s1.get_marks()