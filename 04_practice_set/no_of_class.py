# we are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

list1 = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# since 1 subject -> 1 classroom
# we have to find number of subjects
# but here the number of subjects are not same as the length of list as subjects are repeating 
# to remove redundancy we use sets

print(f"classrooms needed are {len(set(list1))}")