# Create a new file “practice.txt” using python. Add the following data in it:

# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# WAF that replace all occurrences of “java” with “python” in above file.
# Search if the word “learning” exists in the file or not.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")


def replace_text(old, new):
    with open("practice.txt", "r") as f:
        data = f.read()
    
    data = data.replace(old, new)
    with open("practice.txt", "w") as f:
        f.write(data)


def search_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()
        if word in data:
            return True
    return False




replace_text("Java", "python")

print(search_word("learning"))
