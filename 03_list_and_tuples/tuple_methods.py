# tuple has many built-in methods

# t.index(val) returs the first index at which val is present in t

t = (1, 2, 3, 4, 3, 2)
print(t.index(2)) # 1

# t.count(val) returns the count of how many times val occurs in t

print(t.count(2)) # 2
print(t.count(0)) # 0
