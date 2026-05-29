#Greatest of all number
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))


#Finding Greatest
if (a > b and a > c):
    print("a is the greatest among all")
elif(b > c):
    print("b is the greatest among all")
else :
    print("c is the greatest among all")

#Greatest using built in function
Greatest_number = max(a,b,c)
Smallest_number = min(a,b,c)
print("Greatest among all is :",Greatest_number)   
print("Smallest among all is :",Smallest_number)   
