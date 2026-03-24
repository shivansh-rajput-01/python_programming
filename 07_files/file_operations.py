# python can be used to create, read, write, update and delete files

# our program runs in RAM(volatile memory) the data stored and operations performed vanishes ones the program execution terminates

# if we have to do some calculations and store something so that we can access it after program execution also then we have to store it on permanent memory this can be done using databases or files

# f = open(file_name, mode_to_open) is used to open a file
# f.close() is used to close the file and return the resources back to system

# we can have different modes
# r -> read mode we can only read the file
# w -> write mode we can write in file, if file does not exist creates it if exists then deletes its previous data and writes new
# a -> append mode we can write at the end of file, if file does not exists creates it and appends data at the end of file data does not delete old data
# b, t we can open files in rt, wt, at, rb, wb, ab modes where t represents performing file operations on text file
# and b represents on binary files default is t if we write only r it is same as rt
# + -> combined operations are allowed
# r+ -> allows read and write but cursor is at start of file
# w+ -> allows write and read operations, creates file if it does not exists and truncates the data present in it
# a+ -> allows read and write operations, creates file if it does not exists and appends at end i.e. cursor is at end

f = open("first.txt", "w")

f.write("This is our first file for python file handling") # this function writes to python files

f.close()

f = open("first.txt", "r")

content = f.read() # this function reads entire file and returns the data in string

print(f"file has data: `{content}`")
