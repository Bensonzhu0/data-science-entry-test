def swap(x, y):
    """
    - Swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    x, y = y, x
    print("After swapping: x =", x, ", y =", y)
    return x, y


# Task2 as below 
result1 = swap("Apple", 10)
print("Result 1:", result1)  # Expect -1

result2 = swap(9, 17)
print("Result 2:", result2)  # Expect swapped values and (17, 9)
