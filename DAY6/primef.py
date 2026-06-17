#Prime number using function
def prime(num):
    if num <= 1:
        print("It is not a prime number")
    for i in range(2,num):
     if num % i == 0:
        print("It isnot prime number")
        
        break
     
    print("It is a prime number")

a = int(input("Enter your number or -1 to exit : "))
 
while (a != -1):
    prime(a)
    a= int(input("Enter your number : or -1 to exit "))
    