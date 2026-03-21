# method 1 nested loops

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(i):
        print("* ", end="")
    print()

print()
print("method 2")


# method 2 multiply operator

for i in range(1, n+1):
    print("* " * i)
