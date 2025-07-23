import random
#Ex_1

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

#Ex_2

for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

#Ex_3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_input = input('Please write the name ')
try:
    print(names.index(user_input))
except ValueError:
    print(f'{user_input} is not in the list of names')

#Ex_4

first_user_number = input('Please write your first number ')
second_user_number = input('Please write your second number ')
third_user_number = input('Please write your third number ')

if first_user_number > second_user_number:
    if first_user_number > third_user_number:
        print(f'The greatest number is {first_user_number}')
    else:
        print(f'The greatest number is {third_user_number}')
else:
    if second_user_number > third_user_number:
        print(f'The greatest number is {second_user_number}')
    else:
        print(f'The greatest number is {third_user_number}')

#Ex_5

alphabet_string = ''
vowels = list('aoeui')
for i in range(ord('a'), ord('z') + 1):
    alphabet_string += chr(i)

for letter in alphabet_string:
    if letter in vowels:
        print(f'Letter {letter} is a vowel')
    else:
        print(f'Letter {letter} is a consonant')

#Ex_6

user_list_of_words = []
for word in range(7):
    user_list_of_words.append(input('Please write a new word '))
letter = input('Please write a single letter ')

for word in user_list_of_words:
    if letter in word:
        print(f'In word {word} a letter "{letter}" has index {word.index(letter)}')
    else:
        print(f'In word {word} there is no letter "{letter}"')

#Ex_7

list_of_million_numbers = []
for i in range(1, 1000001):
    list_of_million_numbers.append(i)

print(min(list_of_million_numbers))
print(max(list_of_million_numbers))
print(sum(list_of_million_numbers))

#Ex_8

user_list_of_num = list(input('Please write your numbers ').split(','))
user_tuple_of_num = tuple(user_list_of_num)
print(user_list_of_num)
print(user_tuple_of_num)

#Ex_9

user_number = int(input('Please choose the number from 1 to 9 '))
random_number = random.randint(1, 9)

if user_number == random_number:
    print('You are winner')
else:
    print('Better luck next time')

#Bonus_1
random_number = random.randint(1, 9)

while True:
    try:
        user_number = int(input('Please choose the number from 1 to 9. If you want to quit, write "quit" '))
    except ValueError:
        break
    if user_number == random_number:
        print('You are winner')
        break
    else:
        print('Better luck next time')

#Bonus_2
random_number = random.randint(1, 9)

num_of_win = 0
num_of_lose = 0
while True:
    try:
        user_number = int(input('Please choose the number from 1 to 9. If you want to quit, write "quit" '))
    except ValueError:
        break
    if user_number == random_number:
        print('You are winner')
        num_of_win += 1
    else:
        print('Better luck next time')
        num_of_lose += 1

print(f'You won {num_of_win} times. You lose {num_of_lose} times.')





