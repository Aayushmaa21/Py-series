#Passing name and marks of 3 subject

class Student:
    def __init__(self,name,OOP,Stat,MP):
        self.name = name
        self.OOP = OOP
        self.MP =MP
        self.Stat = Stat
    def aveg(self):
        average = (self.OOP +self.MP+self.Stat)/3
        return average
s1 = Student("Aayushma",98,96,100)
s2 = Student("Yuna",94,91,94)
s3 = Student("Sohan",99,95,98)

print(s1.name,s1.OOP,s1.Stat,s1.MP)
print(s2.name,s2.OOP,s2.Stat,s2.MP)
print(s3.name,s3.OOP,s3.Stat,s3.MP)


print(f"Average of {s1.name} is {s1.aveg()}")
print(f"Average of {s2.name} is {s2.aveg()}")
print(f"Average of {s3.name} is {s3.aveg()}")