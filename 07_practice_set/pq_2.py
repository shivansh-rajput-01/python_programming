# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

def find_line(word):
    with open("practice.txt", "r") as f:
        line_no = 1
        for line in f:
            if word in line:
                return line_no
            line_no += 1
    return -1


print(find_line("learning"))
