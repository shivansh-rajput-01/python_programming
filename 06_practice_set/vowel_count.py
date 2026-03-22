# WAF to count vowels in a string

n = input("Enter a string: ")

def count_vowel(str1):
    count = 0
    str1 = str1.lower()
    for i in str1:
        if i == 'a' or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    return count


print(count_vowel(n))
