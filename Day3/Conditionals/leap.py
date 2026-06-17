# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
#    if(year%4 != 0): #4 le divide vayena vane execute hunxa
#        print("It is not leap year")
#    elif (year%100 != 0): #y%4 ==0 && y%100 !=0 ---> leap year
#         print("It is leap year")
#    elif (year%400 == 0) : #400 le divide vyaena vane isnot leap year elsee leap year (else ko conditon ma 400 e divide hunxa ta so)
#         print("It is  leap year")
#    #else:
#        # print("It is a leap year")


# Another way
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")

elif year % 400 == 0:
    print("It is a leap year")

elif year % 100 == 0:
    print("It is not a leap year")

elif year % 4 == 0:
    print("It is a leap year")

else:
    print("It is not a leap year")