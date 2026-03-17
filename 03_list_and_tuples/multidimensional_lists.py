# we can create multidimensional lists in python
# use [[1,3],[2,4],[5,7]] this is a 2d list

list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(list1) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list1[0][1]) # 2 this is indexing in 2d list go to 0 index i.e. [1, 2, 3] then go to index 1 i.e. 2

# consider first [] to travel over arrays as below

# indexes       0          1          2
# array -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# i.e. 0 index -> [1, 2, 3], 1 index -> [4, 5, 6], 2 index -> [7, 8, 9]
# list[0] will be [1, 2, 3] then if we have to take 3 from this we write [1, 2, 3][2] so list[0][2] will do the same


print(list1[0]) # [1, 2, 3]
print(list1[1]) # [4, 5, 6]
print(list1[2]) # [7, 8, 9]

print(list1[0: 2]) # [[1, 2, 3], [4, 5, 6]]
print(list1[0][0: 2]) # [1, 2]
