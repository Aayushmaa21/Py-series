var = 2 
#variable that exists outside a function has scope inside the function body
 
 
def mult_by_var(x):
    return x * var
 
 
print(mult_by_var(7)) # outputs: 14