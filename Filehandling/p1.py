def forline(words):
    with open("Practice.txt","r") as f:
        data = True
        lineno = 1
        while data :
              data = f.readline()
              if(words in data):
                    print(lineno)
                    return
              lineno += 1
    return -1  
            
      


with open("Practice.txt","w") as f:
        f.write("Hi everyone\nWe are learning filehandling in Java")
        f.write("\nusing Java.\nI love programming.")
word = "learning"
with open("Practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found") 
        else:
            print("not found")

new_data = data.replace("Java","Python")

with open("Practice.txt","w") as f:
        f.write(new_data)
forline("learning")
print(forline("hello"))


