# Revising functions, loops, and lists

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [2, 4, 6, 8]
result = calculate_sum(nums)

print("Sum of list:", result)