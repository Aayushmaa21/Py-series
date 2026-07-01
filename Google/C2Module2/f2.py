import os

os.remove("filepath.py") #remove file


#os.rename("orign name",renme)
os.rename("spd.txt","aayu.txt")

#To check if file exist or not
print(os.path.exists("aayu.txt"))

print(os.path.exists("spd.txt"))
