# tup[idx]
# we can use index and slicing as lists
# tup[idx] = val is not valid

tup1 = (1, 2, 3, 4, 5)

print(tup1[0]) # 1
print(tup1[1:4]) # (2, 3, 4)
print(tup1[::-1]) # (5, 4, 3, 2, 1)

# tup1[0] = 100 # error as tuples are immutable in python