import os
#To check whats file size we need to check getsize
a = os.path.getsize("aayu.txt")
print(a)

#To check when file was last modified
b = os.path.getmtime("aayu.txt")
print(b) #Represents no of sec from 1970

