import copy # imported for deep copy

list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print(list1) # [1, 2, 3, 4]
print(list2) # [1, 2, 3, 4]
# we appended in list2 but element is also added in list1
# this is because it is a assignment
# that means they are referring to same array

# to solve this we make shallow copy of list
list3 = list1.copy()
list3.append(5)

print(list3) # [1, 2, 3, 4, 5]
print(list1) # [1, 2, 3, 4]

# effect in nested lists

list4 = [[1, 2, 3], [4, 5, 6]]
list5 = list4

list5[0].append(4)
print(list5) # [[1, 2, 3, 4], [4, 5, 6]]
print(list4) # [[1, 2, 3, 4], [4, 5, 6]]

list6 = list4.copy()

list6[1].append(7)
print(list6) # [[1, 2, 3, 4], [4, 5, 6, 7]]
print(list4) # [[1, 2, 3, 4], [4, 5, 6, 7]] changes are reflecting in shallow copy also why?
# this is because this function makes upper level copy only if nested lists are present it is referenced as it is as in original

list7 = copy.deepcopy(list4)
list7[1].append(8)
print(list7) # [[1, 2, 3, 4], [4, 5, 6, 7, 8]]
print(list4) # [[1, 2, 3, 4], [4, 5, 6, 7]]
