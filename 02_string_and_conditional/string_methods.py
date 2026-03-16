# there are many built in string methods that python provides some of them are discussed below

# finding length of string

# len() is used

str1 = "keshav rajput"
print(len(str1)) # 13

# s.endswith(substr) finds whether s ends with substr

print(str1.endswith("put")) # True
print(str1.endswith("keshav")) # False

# s.replace(old, new) -> replaces all old with new

str2 = "we are studying js"

print(str2.replace("js", "python")) # we are studying python
print(str2) # we are studying js the replace method not changed js with python in original string


# s.capitalize() makes the first letter capital

print(str1.capitalize()) # Keshav rajput

# s.find(substr) -> returns the first index of substr in s if not present return -1

print(str2.find("js")) # 16
print(str2.find("python")) # -1

# s.count(substr) finds how many times substr occurs in s

print(str1.count("a")) # 2
print(str1.count("s")) # 1

# s.strip() this removes heading and trailing spaces

print("    hello world     ".strip()) # hello world

# s.split(seperator) this spilts string on basis of seperator to list
# example "hi,bye,namaste".split(",") will split string into list based on "," so list is ["hi", "bye", "namaste"]

str3 = "hi,bye,namaste"
print(str3.split(",")) # ['hi', 'bye', 'namaste']

# s.isdigit() returns True if s is a number

print("25".isdigit()) # True
print(str1.isdigit()) # False

# s.lower() converts string to lowercase
# s.upper() converts string to uppercase

print(str1.upper()) # KESHAV RAJPUT
print(str1.lower()) # keshav rajput
