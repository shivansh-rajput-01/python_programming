# list the items of list which starts with s

list1 = ["shivansh", "keshav", "madhav", "govind", "shyam", "sundar"]

for ele in list1:
    if ele.lower().startswith("s"):
        print(ele, end = " ")

print()