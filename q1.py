def swap(x, y):
    """
    - Swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    # Check if x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values
    x, y = y, x
    
    # Print swapped values
    print("After swapping: x =", x, ", y =", y)
    return x, y  # Return swapped values in case we need them
