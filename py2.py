import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number where the sum of the factorial of its digits is equal to the number itself.
    """
    if num < 0:
        return False
    
    sum_of_factorials = 0
    original_num = num
    
    # Calculate factorial of each digit and sum them
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

# Iterate through numbers from 1 to 5000 and print strong numbers
print("Strong numbers between 1 and 5000 are:")
for i in range(1, 5001):
    if is_strong_number(i):
        print(i)