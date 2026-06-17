def leap(year):
    if (year%100 and year %400==0 ):
        print("It is leap year")
    elif(year%100 != 0 and year%4 ==0):
        print("It is leap year")
    else:
        print("It is not leap year")



leap(2026)
leap(2016)