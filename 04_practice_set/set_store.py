# store 9 and 9.0 in set

set1 = {9, 9.0}
set2 = {
    9,
    "9.0"
}
set3 = {
    ("int", 9),
    ("float", 9.0)
}


print(set1)
print(set2)
print(set3)

# outputs
# {9}
# {9, '9.0'}
# {('int', 9), ('float', 9.0)}