# dictionary in python are used to store key: value pairs
# dictionary are unordered and mutable
# they are created using {}
# keys in dictionary are unique i.e. one key can come single time only
# the keys can be of immutable types only i.e. they cannot be list, dictionaries or sets
# the values can be of any type

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

# in above example we have used a dictionary as a value to key "subjects" this is known as nested dictionary

print(dict1) # {'name': 'Keshav Rajput', 'subjects': {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}}

dict2 = {
    1: "hello",
    1.1: 1,
    True: False,
    (1, 2, 3): [1, 2, 3]
}

print(dict2) # {1: False, 1.1: 1, (1, 2, 3): [1, 2, 3]}

# accessing values
# dict['key'] returns the value of key in dict

print(dict1['name']) # Keshav Rajput
# print(dict1["age"]) # error as age is not a key

# updating values and inserting values
# dict['key'] = value this updates the value of key if it exists or inserts the key: value pair if key does not exist in dict

dict1['age'] = 14
print(dict1) # {'name': 'Keshav Rajput', 'subjects': {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}, 'age': 14}
# this inserted age: 14 in dict1

dict1['age'] = 11
print(dict1) # {'name': 'Keshav Rajput', 'subjects': {'maths': 100, 'physics': 100, 'Chemistry': 100, 'english': 100, 'python programming': 100}, 'age': 11}
# this updated the value of age to 11 in dict1
