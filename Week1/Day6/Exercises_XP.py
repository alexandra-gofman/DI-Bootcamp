# #Ex_1
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# new_dict = dict(zip(keys, values))
# print(new_dict)
#
# #Ex_2
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = 0
# for key in family.keys():
#     if 3 <= family[key] <= 12:
#         print(f'{key}`s ticket price is $10')
#         total += 10
#     elif family[key] > 12:
#         print(f'{key}`s ticket price is $15')
#         total += 15
#     else:
#         print(f'{key}`s ticket price is $0')
# print(f'Total cost of tickets is {total}')

# #Bonus
#
# family = {}
# num_of_family_members = int(input('Please enter number of the family members: '))
# for i in range(num_of_family_members):
#     key = input('Please enter a name :')
#     value = int(input(f'Please enter an age for {key}: '))
#     family[key] = value
# print(family)
#
# total = 0
# for key in family.keys():
#     if 3 <= family[key] <= 12:
#         print(f'{key}`s ticket price is $10')
#         total += 10
#     elif family[key] > 12:
#         print(f'{key}`s ticket price is $15')
#         total += 15
#     else:
#         print(f'{key}`s ticket price is $0')
# print(f'Total cost of tickets is {total}')

# #Ex_3
#
# brand = {
# 'name': 'Zara',
# 'creation_date': 1975,
# 'creator_name': 'Amancio Ortega Gaona',
# 'type_of_clothes': ['men', 'women', 'children', 'home'],
# 'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 'number_stores': 7000,
# 'major_color':
#     {'France': 'blue',
#     'Spain': 'red',
#     'US': ['pink', 'green']}
# }
# brand['number_stores'] = 2
# print(f"Zara customers buying clothes/ accessories for {', '.join(brand['type_of_clothes'])}.")
# brand['country_creation'] = 'Spain'
#
# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
#
# brand.pop('creation_date')
#
# print(brand['international_competitors'][-1])
# print(brand['major_color']['US'])
# print(len(brand))
# print(brand.keys())
# print(brand)
#
# #Bonus
# more_on_zara = {
# 'creation_date': 1975,
# 'number_stores': 7000
# }
#
# brand.update(more_on_zara)
# print(brand)

#Ex_4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_dict_1 = {}
for i, user in enumerate(users):
    users_dict_1[user] = i

users_dict_2 = {}
for i, user in enumerate(users):
    users_dict_2[i] = user

users.sort()
users_dict_3 = {}
for i, user in enumerate(users):
    users_dict_3[user] = i
