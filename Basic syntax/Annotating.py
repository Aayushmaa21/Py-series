#Annotating is adding information about what type of data a variable is expected to store
age: int = 19
name: str = "Aayushma" 

marks: list[int] = [80, 75, 90]

def add(a: int, b: int) -> int: #It  means function will return int
    return a + b