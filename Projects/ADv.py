#The lost Crystal Adventure
import sys
print("Welcome surviver!!")
print("You are walking on hike and you find a map leading to a lost crystal")
print("What would you do??")
print("A. Enter the forest  B.Walk to the mountain")

choice = input("Enter your choice ")

if choice == 'A':
    print("You hear a strange sound.")
    print("A. Follow the sound B.Climb a tree")
    c2 = input("Enter your choice ")
    
    if c2 == 'A':
        print("You find a hidden cave.")
        print("A. Enter the cave B.Look around outside")
        c3 = input("Enter you choice ")
        if c3 == "A":
            print("You are one step away fron you goal!!")
            print("Congrats,surviver!! You have officially entered the final level ")
            print("Inside the cave is a glowing door.")
            print("A. Open it B.Ignore it")
            c8 = input("Enter your choice ")
            if c8 == 'A':
                print("Congrats!! You WONN")
            else:
                print("Oops! You missed the treasure")
                sys.exit()

        else :
            print("You are dead!! Game over!!")
            sys.exit()
        
    else:
        print("You spot an old treehouse.")
        print("A. Go inside B. Keep walking")
        c4 =  input("Enter you choice ")
        if c4 == 'A':
            print("You are one step away fron you goal!!")
            print('Inside is a treasure map.')
            print("A. Follow the map B. Leave it")
            c9 = input("Enter your choice ")
            if c9 == 'A':
                print("Crystal Found!! You WONN")
            else:
                print("Oops! You missed the treasure")
                sys.exit()

        else :
            print("You will keep walking on a wrong path! Game over!!")
            sys.exit()
else:
    print("A narrow path splits in two.")
    print("A. Take the steep path  B. Take the safe path ")
    c5 = input("Enter you choice ")
    if c5 =='A':
        print("You discover an eagle's nest.")
        print("A. Check the nest B. Move on")
        c6 = input("Enter your choice ")
        if c6 == 'A':
            print("Congrats!! You found golden key")
            print("A. Take key B.Leave key")
            c10 = input("Enter your choice ")
            if c10 == 'A':
                print("Opens Crystal Chamber!! You WONN")
            else:
                print("Cannot open chamber.")
                sys.exit()
            
        else :
            print("Wishing best journery ahead!! Game over")
            sys.exit()
    
    else:
        print("You find a waterfall.")
        print("A. Go behind it B. Follow the river")
        c7 = input("Enter your choice ")
        if c7 == 'A':
            print("You found secret room")
            print("A.Enter room B.tay outside")
            c11 = input("Enter your choice ")
            if c11 == 'A':
                print("Crystal Found!! You WONN")
            else:
                print("Adventure Ends. GAME OVER!!")
                sys.exit()
            
        else:
            print("You cant make it to the end,Game over!!")
            sys.exit()





        

