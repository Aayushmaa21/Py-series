def facto(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *=i
    return fact
    


n = int(input("Enter number which factorial is to be found : "))
print("The factorial of given numbre is",facto(n))