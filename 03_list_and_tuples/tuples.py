# tuples are immutable data structures in python
# we make it by ()

tup1 = (1, 2, 3)
tup2 = () # empty tuple
tup3 = (1,) # single element tuple
tup4 = (1) # this is considered as integer that's why (1,) comma is necessary for single element tuple

print(type(tup3)) # <class 'tuple'>
print(type(tup4)) # <class 'int'>
