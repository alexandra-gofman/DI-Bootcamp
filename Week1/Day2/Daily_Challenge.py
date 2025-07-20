import random

user_string = input("Write your string. The string must be exactly 10 characters long. ")

if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")

print(user_string[0], user_string[-1])

for letter in user_string:
    print(letter)

user_string = list(user_string)
random.shuffle(user_string)
print(user_string)