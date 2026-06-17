with open("aayu3.txt","r") as z:
    data = z.read()
    print(data)

with open("aayu3.txt","w") as y:
    y.write("I am overwriting youu!!")
   
with open("aayu3.txt", "r") as y:
    print(y.read())

import os
 
os.remove("aayu3.txt")

