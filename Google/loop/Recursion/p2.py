def is_power_of(number, base):
 # Base case: when number becomes 1
    if number == 1:
        return True

    if number < base:
        return False

    if number % base != 0:
        return False

    # Recursive case
    return is_power_of(number // base, base)


print(is_power_of(8,2))     # True
print(is_power_of(64,4))    # True
print(is_power_of(70,10))   # False