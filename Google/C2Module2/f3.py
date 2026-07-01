import os
#To check whats file size we need to check getsize
a = os.path.getsize("aayu.txt")
print(a)

#To check when file was last modified
b = os.path.getmtime("aayu.txt")
print(b) #Represents no of sec from 1970
#To solve it
import datetime
timestamp = os.path.getmtime("aayu.txt")
print(datetime.datetime.fromtimestamp(timestamp))
# we are using fromtimestamp from datetime class and date time module
#for my understanding --> precedence = R to L

#Os.path module takes the info provided by operating system