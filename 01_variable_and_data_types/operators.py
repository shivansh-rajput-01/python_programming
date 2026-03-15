# arithmetic operator

a = 7
b = 5

print(a + b) # addition operator ----- output -> 12
print(a - b) # subtraction operator ----- output -> 2
print(a * b) # multiplication operator ----- output -> 35
print(a / b) # division operator ----- output -> 1.4
print(a // b) # floor division operator ----- output -> 1
print(a % b) # modulo operator ----- output -> 2
print(a ** b) # exponentiation operator ----- output -> 16807

# % operator formula if a % b then calculate a-(b*(a//b))

# relational operators

# these include ==, !=, >, >=, <, <=
# always give boolean results i.e. True or False

print(a == b) # output -> False
print(a != b) # output -> True
print(a > b) # output -> True
print(a >= b) # output -> True
print(a < b) # output -> False
print(a <= b) # output -> False

# logical operators

# and, or , not

# works on conditions(boolean)

# and TT
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# or TT
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# and working
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

# or working
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

# not working
print("not True: ",not True)
print("not False: ",not False)

# assignment operator

# =, +=, -=, *=, /=, %=
c = a
d = b
c += d
