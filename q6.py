def find_first_negative(lst):
    """
    - Finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        return -1

    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


# Task2 as below 
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Result 1:", result1)  # -1

result2 = find_first_negative([2, 10, 7, 0])
print("Result 2:", result2)  # "No negatives"
