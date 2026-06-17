#Positional argument nad keyword argument
def greet(name, age, city):
    print(name, age, city)

greet("Ram", 20, city="Kathmandu")   
greet(name="Ram", age=20, city="Kathmandu")  
greet("Ram", age=20, city="Kathmandu")  

#greet(name="Ram", 20, city="Kathmandu")  # SyntaxError