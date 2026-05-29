a = input("Enter your word :")

for _ in range(100000) :
    if a == "chupacabra":
        break
    #else:
    print("You are still stuck here, Try again!!")
    a = input("Enter your word :")
    
print("You've succesfully left the loop")
    