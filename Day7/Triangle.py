def triangle(a,b,c) :
    x = "It is not a triangle"
    y = "It is  a triangle"
    if a + b <= c:
        return x
    if a + c <= b:
         return x
    if c + b <= a:
        return x
    return y

print(triangle(2,3,6))


def triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
 
print(triangle(1, 1, 1))
print(triangle(1, 1, 3))