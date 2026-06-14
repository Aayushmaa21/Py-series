
f = open("aayu.txt", "r")

# data = f.read()  yedyo 2 line rakhyo vane cursor end point ma janxa due to which it wont read further file
# print(data)
line1 = f.readline()
line2 = f.readline()
line3 = f.readline() #cant read further data
print(line1)
print(line2)
print(line3) 
print(type(line1))



f.close()