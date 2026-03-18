# WAP to input marks of three subjects and store them in a dictionary

dict1 = {}

subject = input("Enter the name of subject: ")
marks = int(input("Enter marks of this subject: "))

dict1.update({subject : marks})
subject = input("Enter the name of subject: ")
marks = int(input("Enter marks of this subject: "))

dict1.update({subject : marks})
subject = input("Enter the name of subject: ")
marks = int(input("Enter marks of this subject: "))

dict1.update({subject : marks})

print(dict1)