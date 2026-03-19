# write a program to print the table of n

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# write a program to print a list in python using while loop

list1 = ["ironman", "shaktiman", "batman", "superman"]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# write a program to print a tuple using while loop

tup1 = (1, 3, 5, 7)

i = 0
while i < len(tup1):
    print(tup1[i])
    i += 1

# write a program to print a dictionary

dict1 = {
    "name": "shivansh",
    "age": 20
}
i = 0
keys = list(dict1.keys())
while i < len(keys):
    print(f"{keys[i]} -> {dict1[keys[i]]}")
    i += 1
