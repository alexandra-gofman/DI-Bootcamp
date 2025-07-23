#Ex_1

user_number = int(input('Please write your number '))
user_length = int(input('Please write the length '))

list_of_numbers = []
for i in range(1, user_length + 1):
    list_of_numbers.append(i * user_number)

print(list_of_numbers)

#Ex_2

user_string = input('Please write your string ')

char = ''
new_string = ''
for i in range(len(user_string)):
    if user_string[i] != char:
        char = user_string[i]
        new_string += char

print(new_string)