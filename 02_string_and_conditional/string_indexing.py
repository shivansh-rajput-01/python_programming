# [idx] are used for indexing
# -5 -4 -3 -2 -1  -> these are backward indexing
#  h  e  l  l  o
#  0  1  2  3  4  -> these are forward indexing

str = "hello"

print(str[0])

# string slicing

# method 1 -> use forward indexing
# syntax - str[start_idx: end_idx] -> includes start index and excludes ending index

print(str[0:5]) # hello as last index is not included
print(str[:5]) # if start index is missing takes 0
print(str[0:]) # if ending index is missing then takes len(str)

# method 2 -> use backward indexing
# syntax - str[start_idx: end_idx] -> includes start index and excludes ending index

print(str[-5: -1]) # hell as idx -1 is not included
print(str[-5: ]) # hello
print(str[ :-1]) # hell


print(str[:]) # hello

# the actual slicing syntax contains step as third option 
# str[start_idx : end_idx : step]
# the default step value is +1
# and the value of missing start and end index that python auto fills depends on this step value

# Slicing       | StepType    |  Default Start |  Default Stop
# str[:stop]    | Positive(+1)|  0 (Start)     |  stop
# str[start:]   | Positive(+1)|  start         |  End of string
# str[:stop:-1] | Negative(−1)|  −1 (Last char)|  stop
# str[start::-1]| Negative(−1)|  start         |  Beginning of string

print(str[::-1]) # this reverses the string as in -1 steps default start is -1 index and default end is start of string

# we cannot manipulate using indexes like str[0] = "a" throws error

# if str[10] is written and this index does not exist then index error is thrown but for case of str[0: 100] no error is thrown
# only the valid index values are displayed

# we can give jumps of 2, 3, 4 and so on

print(str[::2]) # prints even index values
