# continue keyword skips the particular iteration taking the flow of loop to the starting of loop

# WAP to print even number between 1 and 100
for i in range(1, 100):
    if(i % 2 != 0):
        continue # skip printing when number is odd
    print(i)
