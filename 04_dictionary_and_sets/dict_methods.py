# dictionary in python have many built-in methods

# finding length i.e. number of keys in dictionary
# len() is used

dict1 = {
    "name": "Keshav Rajput",
    "subjects": {
        "maths": 100,
        "physics": 100,
        "Chemistry": 100,
        "english": 100,
        "python programming": 100
    }
}

print(len(dict1)) # 2

# finding the keys of dictionary
# dict.keys() method returns dict_keys(['key1', 'key2'])

print(dict1.keys()) # dict_keys(['name', 'subjects'])
# this can be converted into python list
print(list(dict1.keys())) # ['name', 'subjects']

# finding values in python dictionary
# dict.values() is used returns dict_values(['val1', 'val2'])

print(dict1.values()) # dict_values(['Keshav Rajput', {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}])

print(list(dict1.values())) # ['Keshav Rajput', {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}]

# finding list of tuples of key: value pairs
# dict.items() returns list of tuples of key: value pairs

print(dict1.items()) # dict_items([('name', 'Keshav Rajput'), ('subjects', {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100})])

# getting values from keys safely
# dict['key'] will give error if 'key' is not present in dict
# dict.get('key') will give None if 'key' is not present in dict

print(dict1.get('name')) # Keshav Rajput
print(dict1.get('age')) # None

# updating values in dictionary
# dict.update(new_dict)
# used to add single or multiple key value pairs at a time

dict1.update({'age': 11, "percentage": 100})
print(dict1) # {'name': 'Keshav Rajput', 'subjects': {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}, 'age': 11, 'percentage': 100}

# deleting key: value pair

# dict.pop(key) it deletes the specified key and returns its value

print(dict1.pop('age')) # 11
# print(dict1.pop('age')) # throws error because age no more exists in dictionary

# clearing complete dictionary
# dict.clear()

print(dict1.clear()) # None
