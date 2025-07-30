#Ex_1

user_word = input('Please enter a word: ')
user_word_list = list(user_word)

user_word_dict = {}
for i, letter in enumerate(user_word_list):
    if letter in user_word_dict.keys():
        user_word_dict[letter].append(i)
    else:
        user_word_dict[letter] = [i]

#Ex_2
items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"

wallet = int(wallet[1:])
affordable_items = []

for key, value in items_purchase.items():
    if ',' in value:
        value = value.replace(',', '')
    if int(value[1:]) < wallet:
        affordable_items.append(key)

affordable_items.sort()
if len(affordable_items) == 0:
    print('Nothing')
else:
    print(affordable_items)

