#error ocuurs in case of floating or other
value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)


try :  #provided code ay cause error
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except : #apply if error occurs
    print("I dont know solution")
