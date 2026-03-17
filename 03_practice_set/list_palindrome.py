list1 = [1, 2, 3]
list2 = [1, 2, 1]

list1_copy = list1.copy()
list1_copy.reverse()
if(list1 == list1_copy):
    print(f"{list1} is a palindrome")
else:
    print(f"{list1} is not a palindrome")

list2_copy = list2.copy()
list2_copy.reverse()
if(list2 == list2_copy):
    print(f"{list2} is a palindrome")
else:
    print(f"{list2} is not a palindrome")
