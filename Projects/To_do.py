my_task=[]

while True:
    print("Welcome to your python TaskTrack")
    print("What are  your plans today!??")
    print("1.Add Task")
    print("2.View Task")
    print("3.Exit")
    
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        task = input("Enter Your Task: ")
        my_task.append(task)
        print("Task Added")

    elif choice == 2:
        print("Your task is to",my_task)
    elif choice == 3:
        break



