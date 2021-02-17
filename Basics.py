#
# Python Basics
#

# Learn print and its format
print("hello")
name = "John"
print("Hello, %s!" % name)

# Get an input
name = input("type name and press enter: ")
print("Hello {0}! Welcome to {1} science.".format(name, 'computational'))

# Assigning variables
a = 4513
b = "why"
c = len(b)

# Learn Lists
list_ex = [4,1,'a',5,14,'12','a521sa']

# Learn Dictionaries
# Either create an empty dict and add key:value pairs or assign one
# A dictionary can store both string and number as keys
# It can even store a list as value
dict_ex = {'try': 'not',
           'key': 2}
pass # to avoid PEP complaining
dict_ex['key'] = 2**2  # this mean exponentiation
dict_ex[2] = 'word'
dict_ex['list'] = list_ex

# Learn Conditional flow
# If statement
if a == 1:
    print(a)
else:
    print(0)
# or short form:
print(b) if b != 1 else print(b)

# For statement
# range(a,b) return a list from a to b-1
for i in range(0, 5):
    print(i)

# Read files
directory = "some kind of directory"

file = open(directory, 'r')
for raw_line in file:
    new_line = raw_line.rstrip("\r\n")  # to strip carriage return and newline
    words = new_line.split('')  # split the line into a list of words
file.close()

# Write files
file = open(directory, 'w')
file.write(" Write something here\n")
file.close()

