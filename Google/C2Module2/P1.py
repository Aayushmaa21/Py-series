file = open("spider.txt")
print(file.readline()) #READS 1ST LINE
print(file.readline()) #READS 2ND LINE
print(file.read()) #READS ALL FILE FROM CURRENT POSOTION
file.close()
with open("spider.txt") as file: #"WITH" AUTOMATICALLY CLOSES THE FILE
   # print(file.readline()) #READS 1ST LINE CAUSE WE HAVE ALREADY CLOSED PREVIOUS OPENING
    print(file.read()) 