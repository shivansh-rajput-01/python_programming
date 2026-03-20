# for loop in python is used to iterate over iterables
# or they are used when we want to traverse over a finite number of times

# for loop to print 1 to 10
# range() function can be used with for loop
# range(start, end, step)
# returns a sequence from start to end-1 and the gap of step(default 1)

for i in range(1, 11): # it will go from start(1) to end-1(11-1=10)
    print(i)



# WAP to traverse list using for loop

# in operator is used to traverse over iterables using for loop
list1 = ["hello", "hii", "namaste", "radhe radhe"]
for el in list1: # every element will come one by one in el
    print(el, end=" ") # hello hii namaste radhe radhe

# WAP to traverse a tuple in python using for loop

tup1 = (1, 2, 3, 4, 5)

for i in tup1:
    print(i, end=" ") # 1 2 3 4 5


# WAP to traverse over dictionary using for loop


dict1 = {
    "name": "Keshav Rajput", 
    "age": 11
}

# method 1

for el in dict1.keys():
    print(f"{el} -> {dict1[el]}")

# output
# name -> Keshav Rajput
# age -> 11

# method 2

for key, val in dict1.items():
    print(f"{key} -> {val}")

# output
# name -> Keshav Rajput
# age -> 11

# this is known as tuple unpacking
# since we have studied dict.items() gives list of tuples of (keys, values) in each iteration dict1.items() gives (key, value) tuple so we just unpack it

# tuples unpacking

var1, var2, var3 = (1, 2, 3) # var1 = 1, var2 = 2, var3 = 3
print(f"var1 = {var1}, var2 = {var2}, var3 = {var3}")

var1, _, _, var3 = (1, 2, 3, 4) # var1 = 1 and var3 = 4 all mid values skipped by using "_"
# note here "_" is just a variable that is overwritten multiple times to skip values
print(f"var1 = {var1}, var2 = {var2}")

# this is for_loop basics