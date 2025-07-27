import random

#Ex_1

C = 50
H = 30
D = list(input().split(','))
output = []

for num in D:
    Q = ((2 * C * int(num)) / H) ** 0.5
    output.append(str(round(Q)))

print(','.join(output))

#Ex_2

list_of_int = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

print(list_of_int)
print(sorted(list_of_int, reverse=True))
print(sum(list_of_int))

list_of_first_and_last = []
list_of_first_and_last.append(list_of_int[0])
list_of_first_and_last.append(list_of_int[-1])
print(list_of_first_and_last)

list_greater_fifteen = []
for num in list_of_int:
    if num > 50:
        list_greater_fifteen.append(num)
print(list_greater_fifteen)

list_smaller_than_ten = []
for num in list_of_int:
    if num < 10:
        list_smaller_than_ten.append(num)

print(list_smaller_than_ten)

list_of_squared_num = []
for num in list_of_int:
    list_of_squared_num.append(num ** 2)
print(list_of_squared_num)

set_of_int = set(list_of_int)
len_of_set_of_int = len(set_of_int)
list_of_int_without_duplicates = list(set_of_int)
print(f'In new list {list_of_int_without_duplicates} there are {len_of_set_of_int} numbers')

print(sum(list_of_int) / len(list_of_int))

print(max(list_of_int))
print(min(list_of_int))

sum_of_int = 0
for num in list_of_int:
    sum_of_int += num
print(sum_of_int)

avg_of_int = sum_of_int / 10
print(avg_of_int)

min_of_int = list_of_int[0]
for num in list_of_int:
    if num < min_of_int:
        min_of_int = num
print(min_of_int)

max_of_int = list_of_int[0]
for num in list_of_int:
    if num > max_of_int:
        max_of_int = num
print(max_of_int)

user_list_of_int = []
temp_list = []
for i in range(10):
    temp_list = list(input('Please write 10 integers in range from -100 to 100 ').split(' '))
    j = 0
    for num in temp_list:
        temp_list[j] = int(num)
        j += 1
    user_list_of_int += temp_list
    temp_list = []
print(user_list_of_int)

list_of_random_int = []
for i in range(10):
    list_of_random_int.append(random.randint(-100, 100))
print(list_of_random_int)

len_of_list_of_random_int = random.randint(1, 50)
list_of_random_int = []
for i in range(len_of_list_of_random_int):
    list_of_random_int.append(random.randint(-100, 100))
print(list_of_random_int)

#Ex_3

text = """Last weekend, I decided to visit the park near my house.
The weather was sunny and warm, so many people were walking their dogs and playing with their children.
I sat on a bench, listened to music, and watched the clouds slowly move across the sky.
Later, I bought an ice cream and enjoyed the peaceful afternoon.
It was a simple day, but it made me feel relaxed and happy."""

print(text)
print(f'This text contains {len(text)} characters')

num_of_sentences = 0
num_of_words = 0
num_of_char_without_ws = 0
for char in text:
    if char == '.':
        num_of_sentences += 1
    if char == '.' or char == ' ':
        num_of_words += 1
    if char != ' ':
        num_of_char_without_ws += 1

print(f'This text contains {num_of_sentences} sentences')
print(f'This text contains {num_of_words} words')


new_text = text.replace(',', '')
new_text = new_text.replace('.', '')
new_text = new_text.replace('\n', ' ')
list_of_words = new_text.split(' ')
for i, word in enumerate(list_of_words):
    list_of_words[i] = word.lower()
set_of_words = set(list_of_words)
print(f'This text contains {len(set_of_words)} unique words')

print(f'This text contains {num_of_char_without_ws} characters without whitespaces')
print(f'This text contains {round(num_of_words / num_of_sentences)} average amount of words per sentence')
print(f'This text contains {len(list_of_words)} non-unique words')


#Ex_4

user_str = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
list_of_words_in_str = user_str.split(' ')
set_of_words_in_str = set(list_of_words_in_str)
for word in set_of_words_in_str:
    print(f'{word}:{user_str.count(word)}')