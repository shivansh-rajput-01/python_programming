# break keyword is used in python to take the control of program out of while loop

# write a program to find/ seach an element in a python list

list = [1, 7, 5, 2, 3, 6, 4]

element = 1

idx = 0

for i in list:
    print("loop run")
    if i == element:
        print(f"{element} found at index {idx} of {list}")
    idx += 1

# in this code loop runs even after finding the element which is not efficient as we are traversing over entire list after finding element also
# output
# loop run
# 1 found at index 0 of [1, 7, 5, 2, 3, 6, 4]
# loop run
# loop run
# loop run
# loop run
# loop run
# loop run

list = [1, 7, 5, 2, 3, 6, 4]

element = 1

idx = 0

for i in list:
    print("loop run")
    if i == element:
        print(f"{element} found at index {idx} of {list}")
        break # in iteration where element is found take the control out of loop
    idx += 1

# output
# loop run
# 1 found at index 0 of [1, 7, 5, 2, 3, 6, 4]
