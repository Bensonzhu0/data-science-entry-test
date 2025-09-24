def string_reverse(s):
    """
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return -1
    
    return s[::-1]


# Task 2 as below 
result1 = string_reverse("Hello World")
print("Result 1:", result1)  # "dlroW olleH"

result2 = string_reverse("Python")
print("Result 2:", result2)  # "nohtyP"
