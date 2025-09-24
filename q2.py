def find_and_replace(lst, find_val, replace_val):
    """
    - Searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):   # validate input
        return -1

    # Replace all occurrences
    lst = [replace_val if item == find_val else item for item in lst]
    return lst


# Task 2 as below 
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Result 1:", result1)  # [1, 5, 3, 4, 5, 5]

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Result 2:", result2)  # ['orange', 'banana', 'orange']
