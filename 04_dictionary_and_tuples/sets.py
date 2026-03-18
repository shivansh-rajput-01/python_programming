# sets are unordered collection of unique immutable objects
# sets are  mutable but their elements should be immutable
# as mutable objects are not hashable
# set only takes unique values

set1 = {1, 2, 2, 3, 3, 3}

print(set1) # {1, 2, 3}

# creating an empty set

set2 = {} # this is actually an empty dictionary not a set

print(type(set2)) # <class 'dict'>

set2 = set() # this is an empty set

print(type(set2)) # <class 'set'>