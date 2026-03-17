# we can do indexing and slicing in lists similar to strings

# list[idx]
# list[start_idx: end_idx]
# list[start_idx: end_idx: step]

list1 = [1, 2, 3, 4, 5, 6, 7]

print(list1[0]) # 1
# print(list1[7]) # error

print(list1[0:10]) # [1, 2, 3, 4, 5, 6, 7] no error like string in extra slice

print(list1[::2]) # [1, 3, 5, 7]
print(list1[::-1]) # [7, 6, 5, 4, 3, 2, 1] this reverses the list
print(list1) # [1, 2, 3, 4, 5, 6, 7]
