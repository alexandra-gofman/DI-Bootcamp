#Ex_1

user_string = input('Enter your string: ')
user_string = user_string.replace(' ', '')
user_list = user_string.split(',')
user_list.sort()
sorted_string = ','.join(user_list)
print(sorted_string)

#Ex_2

def compare_words(user_text):
    user_list = user_text.split(' ')
    winner_index = 0
    winner_len = 0
    for i, word in enumerate(user_list):
        if len(word) > winner_len:
            winner_len = len(word)
            winner_index = i
        else:
            continue

    return user_list[winner_index]


user_text = input('Please enter your string: ')
print(compare_words(user_text))