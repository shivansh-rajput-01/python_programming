# print unique numbers from list with their frequencies

numbers = [1, 2, 3, 2, 1, 4, 5, 2, 4, 1, 0]
dict1 = {}

for num in numbers:
    if num in dict1:
        dict1[num] += 1
    else:
        dict1[num] = 1

for key, val in dict1.items():
    print(f"{key} : {val}")
