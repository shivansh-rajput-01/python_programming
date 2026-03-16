# find the largest of three numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 > num2:
    if num1 > num3: # if num1 is larger than num2 then check b/w num1 and num3 which is larger
        print(f"{num1} is largest")
    else:
        print(f"{num3} is largest")
else: # id num2 >= num1
    if num2 > num3: # if num2 is larger than num1 then check b/w num2 and num3
        print(f"{num2} is largest")
    else:
        print(f"{num3} is largest")
