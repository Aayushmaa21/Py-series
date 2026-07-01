import os
file= "aayu.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print("File not found")


#abs takes the file and convert it into its absolaute path
a = os.path.abspath("aayu.txt")
print(a)