def check_divisibility(num, divisor):
    """
    - Check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1
    
    if divisor == 0:
        return False  # cannot divide by zero
    
    return num % divisor == 0


# Task 2 as below 
result1 = check_divisibility(10, 2)
print("Result 1:", result1)  # True

result2 = check_divisibility(7, 3)
print("Result 2:", result2)  # False
