#1
first = 'Hello World'

#2
#This is a comment

#3
print('I AM A COMPUTER')

#4
if 1 < 2 and 4 > 2:
    print('Math is fun')

#5
nope = None

#6
a = True and False
print(a)

#7
print(len("What's my length?"))

#8
b = 'i am shouting'
print(b.upper())

#9
c = '1000'
c = int(c)
print(c, type(c))

#10
a = 4
b = 'real'
print(str(a)+b)

#11
print(3 * 'cool')

#12
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(f'Error: {e}')

#13
print(type([]))

#14
name = input("What's your name? ")
print(f'Your name is {name}')

#15
num = int(input('Write a number '))
if num < 0:
    print(f'{num} is less than 0!')
elif num > 0:
    print(f'{num} is greater than 0!')
else:
    print('You picked 0!')

#16
a = 'apple'
print(a[1])

#17
a = 'xylophone'
index = a.find('y')
if index != -1:
    print(f"There is 'y' in world '{a}'")

#18
a = 'my_string'
if a.islower() is True:
    print(f"the string '{a}' is in lowercase")
