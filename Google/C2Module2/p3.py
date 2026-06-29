
with open("spd.txt") as miles:
    for line in miles:
        print(line.strip().upper())


file = open("spd.txt")
lines = file.readlines() #stores all the lines in OS
file.close()
lines.sort()
print(lines)