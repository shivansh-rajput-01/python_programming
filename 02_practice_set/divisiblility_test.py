num1 = int(input("Enter a number to check divisibility: "))
divisor = int(input("Enter the number to divide: "))

if num1 % divisor == 0:
    print(f"{num1} is divisible by {divisor}")
else:
    print(f"{num1} is not divisible by {divisor}")
