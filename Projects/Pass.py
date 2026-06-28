def pass_checker(a):
    symbols = "!@#$%^&*()_+-={}[]|:;\"'<>,.?/"
    symb = 0
    score = 0
    lower = 0
    Upper = 0
    digit = 0
    length = 0

    if len(a)>=8:
        length = 1
    
    for ch in a:   #Checking each character
        if ch.islower():
            lower = 1
        if ch.isupper():
            Upper = 1
        if ch.isdigit():
            digit = 1
        if ch in symbols:
            symb = 1
    
    score = length + lower + Upper + digit + symb
    if score ==5:
        print("Nicee !! If you remember this, you deserve a medal (*/ω＼*)")
        exit()
    elif score >= 3:
        print("Well!! just emotionally confused ^_~")
    else:
        print("Too weak!! Even a sticky note is safer than this :-)")

print("Welcome to your personal password checker!!")
while True:
    a = (input("Enter Your Password\n"))
    pass_checker(a)
    
    

