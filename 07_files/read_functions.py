# python provides different functions to read file 
# read() method reads entire file at once and returns a string
# readline() method reads a single line and returns a string
# readlines() method reads entire file and returns a list of strings where each string is a line in file

f = open("read_demo.txt", "r")

print(f"read method output -> {f.read()}")
f.seek(0) # this method is used to change the place of cursor to start of file when 0 is passed
print(f"readline method output -> {f.readline()}")
f.seek(0)
print(f"readlines method output -> {f.readlines()}")

f.seek(0)

# now how to use readline to read file line by line when the file ends readline return "" empty string

# method 1
while True:
    data = f.readline()
    if data == "":
        break
    print(data)

f.seek(0)
# method 2 as "" is False in python
while True:
    data = f.readline()
    if not data:
        break
    print(data)

f.seek(0)
# method 3 not readline but to read file line by line
for line in f:
    print(line)

f.close()
