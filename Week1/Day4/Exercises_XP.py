#Ex_1
my_fav_numbers = {4, 24, 20, 283, 52}
friend_fav_numbers = {24, 97, 74, 693}

my_fav_numbers.add(90)
my_fav_numbers.add(4839)
my_fav_numbers.remove(4839)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

#Ex_2
my_tuple = (432, 9, 30, 47, 72)
try:
    my_tuple[5] = 325
except TypeError:
    print('You cannot add new elemets to tuple')
print(my_tuple)

#Ex_3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)

#Ex_4
floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
new_floats = []
for i in range(8):
    new_floats.append(1.5 + i * 0.5)
print(new_floats)

#Ex_5
for i in range(20):
    print(i + 1)

for i in range(20):
    if i % 2 == 0:
        print(i + 1)

#Ex_6
if_user_wrote_my_name = False
while if_user_wrote_my_name == False:
    user_name = input('Please write a name: ')
    if user_name == 'Alexandra':
        print('You exited the loop')
        if_user_wrote_my_name = True
    else:
        print('Try one more time!')

#Ex_7
user_favourite_fruits = input('Write your favourite fruits: ').split(' ')
one_fruit = input('Write a name of fruit: ')
if one_fruit in user_favourite_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it!')
print(user_favourite_fruits)

#Ex_8
topping = ''
list_of_toppings = []
while topping != 'quit':
    topping = input('Please write a topping for pizza: ')
    if topping != 'quit':
        list_of_toppings.append(topping)
        print(f'Adding {topping} to your pizza.')
num_of_toppings = len(list_of_toppings)
total_cost = 10 + num_of_toppings * 2.5
print(f'Total cost is {total_cost}$')

#Ex_9
total_tickets_cost = 0
num_of_family_members = int(input('Please write number of family members: '))
for i in range(num_of_family_members):
    age = int(input('How old are you? '))
    if age > 12:
        total_tickets_cost += 15
    elif age > 3:
        total_tickets_cost += 10
print(f'Total: {total_tickets_cost}$')

#Bonus
list_of_ages = []
list_of_names = []
num_of_guests = int(input('Please write number of guests: '))
for i in range(num_of_guests):
    list_of_ages.append(int(input('How old are you? ')))
    list_of_names.append(input('What\'s your name? '))

new_list_of_ages = []
new_list_of_names = []

i = 0
for age in list_of_ages:
    if (age >= 16) and (age <= 21):
        new_list_of_ages.append(age)
        new_list_of_names.append(list_of_names[i])
    i += 1
attenders = ' '.join(new_list_of_names)
print(f'Attenders: {attenders}')

#Ex_10
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

i = sandwich_orders.count('Pastrami')
while i != 0:
    sandwich_orders.remove('Pastrami')
    i -= 1

finished_sandwiches = []
for i in range(len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders[i])
    print(f'I made your {sandwich_orders[i]} sandwich.')
