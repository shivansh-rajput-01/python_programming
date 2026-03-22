# recursion is a programming technique in which a function calls itself with a smaller value
# i.e. we try to define a recurence relation in which a function calls itself with smaller values until base condition is reached

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))