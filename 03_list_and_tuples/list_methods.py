# list in python has multiple built-in methods
# these methods make changes in original lists

# finding length in lists

list1 = [1, 2, 3, 4, 5, 6, 7]

print(len(list1)) # 7

# l.append(val) adds val to end of list l

print(list1.append(8)) # None it returns None and made changes in original list list1
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8]

# l.sort() this sorts the list in ascending order
# l.sort(reverse=True) this sorts list in descending order

list1.sort(reverse = True)
print(list1) # [8, 7, 6, 5, 4, 3, 2, 1]

list1.sort()
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8]

# l.reverse() reverses the element in list
list1.reverse()
print(list1) # [8, 7, 6, 5, 4, 3, 2, 1]

# l.insert(idx, val) inserts val at idx index of l

list1.insert(0, 100)
print(list1) # [100, 8, 7, 6, 5, 4, 3, 2, 1]

# l.remove(val) removes val from l

list1.remove(100)
print(list1) # [8, 7, 6, 5, 4, 3, 2, 1]
# list1.remove(10) # gives error if val not present

# l.pop(idx) deletes element at index idx of l
list1.pop(1)
print(list1) # [8, 6, 5, 4, 3, 2, 1]
# list1.pop(11) # error

# l.append() vs l.extend()

list1.append([1, 2])
print(list1) # [8, 6, 5, 4, 3, 2, 1, [1, 2]] appended whole list as an element

list1.remove([1, 2])

list1.extend([1, 2])
print(list1) # [8, 6, 5, 4, 3, 2, 1, 1, 2] add all elemnts of list as individual elements

list1.extend("ABC")
print(list1) # [8, 6, 5, 4, 3, 2, 1, 1, 2, 'A', 'B', 'C'] the elements of string are added as individual elements
