# they are used to use logical conditions in our code
# to use block in them we use indentation

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
else:
    while not age.isdigit():
        age = input("Enter age as number: ")
    age = int(age)


if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")

