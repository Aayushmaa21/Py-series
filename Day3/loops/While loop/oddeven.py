num = int(input("Enter the number or -1 to exit: "))

odd = 0
even = 0
seq = 0

while(num!= -1) :
    seq+=1
    if num%2 == 0:
        even +=1
    else :
        odd +=1
    num = int(input("Enter the number or -1 to exit: "))    


print("Odd Sequence is :", odd)
print("Even Sequence is :", even)
print("Total Sequence is :", seq)
