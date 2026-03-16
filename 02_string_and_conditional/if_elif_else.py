num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is largest")
elif num2 > num3 and num2 > num4: # here we can come only if num1 is not largest so check num2 is lagrer than num3 and num4 only
    print(f"{num2} is largest")
elif num3 > num4: # here we can come only if num1 and num2 are not largest check if num3 is larger than num4
    print(f"{num3} is largest")
else: # here we can come only if num1, num2 and num3 are not largest
    print(f"{num4} is largest")

# multiple if then all runs
# if elif ladder then only runs till above one is not true
