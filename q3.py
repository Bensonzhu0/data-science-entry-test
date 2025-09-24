def update_dictionary(dct, key, value):
    """
    - Updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        return -1
    
    if key in dct:
        print("Original value for key '{}':".format(key), dct[key])
    
    dct[key] = value
    return dct


# task2  as below 
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)  # {'name': 'Alice'}

result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2)  # prints original value 25 then {'age': 26}
