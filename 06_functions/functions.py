# functions in python are used to write a block of code that can be invoked(call) at any time and any place of code
# they are used to make our code modular i.e. instead of writing whole logic at once break them into smaller logics
# and integrate them to make our software complete
# unlike loops that repeat same logic multiple times at a single place the function logic can be called any number of times at
# any place
# def keyword is used in python to define a function
# function in python defines a scope that is variables created inside the functions cannot be used outside it

# this is function definition
def sum(a, b): # def is keyword and sum is name of function and a, b are parameters
    return a + b


# a function definion does nothing work is done when the function is called
# function_name() is used to call a function
# if a function does not return anything it returns None in python

s = sum(1, 2) # 1, 2 are the arguments that will be passed in a, b and then sum() returns a+b i.e. return 1+2 = 3 at the place it is called]
# this resolves to s = 3

print(s) # 3

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(fact(4)) # 24
# here fact(4) returned 24 inside print which gets printed

# function without return

def greet1(name):
    print(f"namaste {name}")

greet1("keshav")

# function without parameters and return

def greet2():
    print("namaste")

greet2()


# default parameters
# we can set the default value of parameters in function definition
# if the parameter does not get value from function call then default value will be used
# default parameters should always come after non-default parameters

def prod(a, b=1):
    return a * b

print(prod(1)) # 1
print(prod(1, 5)) # 5

# functions in python are of two types
# built-in functions -> the functions whose definition we do not write and comes in python
# type(), len(), print(), input() are examples of built-in functions

# user defined functions are the functions whose definition we write
# sum(a,b), etc that we write are examples of user defined functions
