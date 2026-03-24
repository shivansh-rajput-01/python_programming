# we generally write files operation in with block
# when using with block we don not need to use f.close() as file auto closes after with block

with open("read_demo.txt", "r") as f:
    while (data := f.readline()): # := is walrus operator in python 3.8+ allows assigment in loop condition
        print(data.strip())

print("file operations completed")
