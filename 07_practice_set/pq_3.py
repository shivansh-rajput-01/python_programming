# From a file containing numbers separated by comma, print the count of even numbers.

def count_even():
    with open("even_count.txt", "r") as f:
        data = f.read()
    l = data.split(",")
    count = 0
    for i in l:
        if int(i) % 2 == 0:
            count += 1
    return count


# count function with self parsing

def count_even_2():
    with open("even_count.txt", "r") as f:
        data = f.read()
    count = 0
    s = ""
    for i in data:
        if i != ",":
            s += i
        else:
            if int(s) % 2 == 0:
                count += 1
            s = ""
    if int(s) % 2 == 0:
        count += 1
    return count


print(count_even())
print(count_even_2())
