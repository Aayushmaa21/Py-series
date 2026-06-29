tocheck = ["Sohan", "Yuna"]
check_in = [ ]


with open("guests.txt","r") as guests:
    for g in guests:
        check_in.append(g.strip())
    for check in tocheck:
        if check in check_in :
            print("{} is checked in".format(check))
        else :
            print("{} isnot checked in".format(check))

