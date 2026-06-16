class Student:
    college ="PK CAMPUS"
    name ="NOIDEA"

    def __init__(self,name,marks):
        self.name = name #Precedence of obj is highher than class
        self.marks = marks
    def hello(self):
        print("Hello",self.name)

s1 = Student("Aayu",98)
s2 = Student("Yuna",96)

print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(Student.college,Student.name)
s1.hello()
s2.hello()