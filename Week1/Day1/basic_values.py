# BASIC VALUE TYPES
#
# COMMENTS = # OR ctrl+/
#
# STRINGS
# text, sequence of characters, defined with a quotation marks "" or ''

'Hello World'

# -Variables like 'boxes where we can store data types (info)

greeting = 'Hello World'

# print() A function that 'prints' something to the console

# -STRING METHODS  = are functions that we can apply into strings
print(greeting.capitalize())
print(greeting.upper())
print(greeting.lower())

#string index
print(greeting[3])

#string slicing
print(greeting[1:5])

#exercise
description = "strings are..."
print(description.upper())
print(description.replace('are', 'is'))
print(description[:7])

# - NUMBERS
#INTEGER = WHOLE NUMBER (NO DEMICAL)
#FLOAT = DEMICALS
#COMPLEX NUMBERS = NUMBERS + LETTERS

my_favourite_number = 7
my_num = complex(3, 5)
my_high = 1.59
print(type(my_high))

# -MATH OPERATIONS WITH NUMBERS

print(5 + 3)
print(5 - ( - 3))
print(5 - 7)
print(5 * 3)
print(15 // 3)

#Math with strings
# \n is a special character that creates a new line
print('Sasha ' * 3)

#COMPARSION OPERATORS

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#BOOLEANS: True and False


