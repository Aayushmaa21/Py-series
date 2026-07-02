import os
#To know directory
print(os.getcwd())

#To make directory
#os.mkdir("newone.dir")

#To change directory
os.chdir("newone.dir")
print(os.getcwd())

#Rm dir to remove dir
#os.mkdir("newone.dir") #It will only work if directory is empty

#we need to remove all files and sub dir before actuallly removing main one
print(os.listdir())

#To find if it is files or dir
directory = "."

for name in os.listdir(directory):
    fullname = os.path.join(directory, name)

    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname)) #print only one cause of else block