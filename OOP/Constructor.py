class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("Adding new student in Database")

s1 = Student("Yuna")
print(s1.name)

s2 = Student("Aayushma")
print(s2.name)