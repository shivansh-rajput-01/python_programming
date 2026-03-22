# print numbers from n to 1

n = int(input("Enter a number: "))

def rev_print(n):
    if n == 0:
        return
    print(n)
    rev_print(n - 1)

# print numbers from 1 to n

def forward_print(n):
    if n == 0:
        return
    forward_print(n - 1)
    print(n)

# here in first program we have written print(n) before rev_print(n-1) which prints n then calls with (n-1) as parameter and prints n-1 then calls with (n-2) as parameter prints n-2 and so on when n == 0 then returns without calling itself

# in second program we keep calling forward_print() with n then n-1 then n-2 without printing when n == 0 then it returns to function call which called it that is forward_print(1) it prints 1 and return to forward_print(2) then prints 2 and so on till n

rev_print(n)
forward_print(10)
