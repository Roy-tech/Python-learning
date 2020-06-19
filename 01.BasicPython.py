# Addition, subtraction
print(7 + 4)
print(3 - 1)

# Multiplication, division, modulo, and exponentiation
print(7 * 6)
print(8 / 2)
print(29 % 7)
print(5 ** 2)

# How much is your $100 worth after 7 years?
print(100 * (1.1) ** 7)

# \n means new line
print('r:\toy\navid')

# \r means new line plus remove everything precedent to \r
print('r:\roy\David')

# r '' string sign helps to print line as it is. Besides, \ can be used to write codes in an argument in multiple lines
print(r'r:\roy\David')

# Create variables with numbers and strings
rate = .10
Sum = 1000
year = 5
Total = round(Sum * (1 + rate) ** year)

# Normal string VS Formatted string
first = 'Marry'
last = 'Jane'
message = first + ' [' + last + '] ' + 'is a good coder!'
print(message)

# a literal string with prefixed f contains expressions inside braces, replacing with their values
msg = f'{first} [{last}] is a damn good coder!' # formatted string
print(msg)

# String function
note = "I will have ${T} in {y} years.".format(T=Total, y=year)
note_copy = "I will have ${} in {} years."
note_copy1 = "I will have ${1} in {0} years." # index numbers to place in the correct placeholders
print(note)
print(note_copy.format(Total, year))
print(note_copy1.format(year, Total))

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out 3rd, last element and kitchen area from areas (Each element in the list is called index)
# (Sequence of the list starts from 0 when it starts from left and -1 when it starts from right end )
print(areas[1])
print(areas[-1])
print(areas[-7])

# Print out the index of the element 20.0
print(areas.index(20))

# string casting, len, object, string slices, replace, split
# String methods, dotnotation, getting user input, random numbers
string = "I would like to learn Python"
print(string[8:])

print(string[:7] + " really " + "love " + string[13:])

print(string.center(50))

print(string.count("n"))

# Use upper() and lower() on string
place_up = string.upper()
place_down = string.lower()

# You can use ; to write two statements or arguments in one line
print(place_up);
print(place_down)

# Finding the index number
print(string.find("learn"))

print(string.join(" "))

# strip() method removes characters from both left and right
print((string.center(50)).strip())

print(len(string))

print(string.replace("I", "You"))
string_new = string.replace("I", "You")
print(string_new.replace("like", "love"))

# Message maintaining gaps and multiple lines
email = '''
Hi Athar,

Hope you are rocking! Here is our first email to you through programming. 

Thank you for your support and cooperation.

Best wishes,
Roy
'''
print(email)

# Create lists of sizes in first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=False)

# Print out full_sorted
print(full_sorted)

# Use append twice to add more sizes
full.append(24.5);
full.append(15.45)

# Reverse the orders of the elements in areas (not in ascending or descending, it will flip the order of the list)
full.reverse()

# Print out full
print(full)

# Importing math package, if you use m, you need to mention that.
import math as m

x = m.sqrt(16)
print(x)

# Otherwise following import methods can be used to directly call for function names
from math import sqrt, pow
from math import *  # * means importing all functions from math

y = sqrt(125)
z = pow(5, 2)

# simple foreach function using string split function and len
city = "California"
for i in city:
    print(i, end=",")

country = ["United States of America", "New Zealand", "Australia", "United Kingdom"]
for i in country:
    print(i, len(i))

# for and range function
print(range(4))
print(list(range(3)))
for i in range(3):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(1, 9, 2):
    print(i)

# small program to guess numbers used by string function, while function
number = "9"
answer = input("please enter a number?")
while True:
    if number == answer:
        break
    answer = input("Please try again!")
print("you are right")

# algorithm + foreach function
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
print(i)
