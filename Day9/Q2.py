try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError: #in case of float 
    print('I do not know what to do.')    
except ZeroDivisionError: #executed if there is zero division error
    print('Division by zero is not allowed in our Universe.') 
except:  # can be any error
    print('Something strange has happened here... Sorry!')
