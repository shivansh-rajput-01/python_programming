# nested loop method 1

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()

print("method 2")

# multiply operator method 2

for i in range(n):
    print("* " * n)