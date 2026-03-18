# sets in python has many built-in methods

# set.add(el) adds el to set

set1 = {1, 2, 3}
set1.add(4)
set1.add(5)
set1.add(6)

print(set1) # {1, 2, 3, 4, 5, 6}

# removing values from set
# set.remove(el) removes el if exists and throws error if el not exists

set1.remove(6)

# set1.remove(7) # error

print(set1) # {1, 2, 3, 4, 5}

# clear the set
# set.clear() makes the set empty

set1.clear()
print(set1) # set()

# removing random value
# set.pop() is used
# it can be used if we have multiple values and want to give random value

set1 = {1, 2, 3, 4, 5}

print(set1.pop()) # 1

# union of sets
# union operation is similar to maths set union
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.union(set2) = {1, 2, 3, 4, 5}
# it returns combined unique values from set1 and set2 in a new set

set2 = {3, 4, 5, 6, 7}

print(set1.union(set2)) # {2, 3, 4, 5, 6, 7}

# intersection
# set1.intersection(set2) gives the set of values common in both set1 and set2

print(set1.intersection(set2)) # {3, 4, 5}
