# WAF to convert USD to INR.

def convert(usd, rate=94.01):
    return usd * rate

u = int(input("Enter the amount in USD: "))

print(f"{u} USD = {convert(u)} INR")

# WAF to print the elements of a list in a single line.

list1 = [1, 3, 2, 4, 5, 7, 6, 8, 9]

def l_display(l):
    for i in l:
        print(i, end = " ")

l_display(list1)
