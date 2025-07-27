# Dictionaries
# Syntax
# {'key': value, 'key': value}

dict_constructor = {
    'name': 'juliana',
    'age': 35,
    'pets': ['caramelo', 'pipoca']
}
student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address': 'Privet Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Gryffindor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}

# ACCESSING DATA
print(student_info['pets'])
print(student_info['pets'][1])

# using methods on the values
student_info['pets'].append('Fenix')
print(student_info['pets'])
print(student_info['first_name'].upper())
student_info['address'] = 'Hogwarts'

# deleting a key
del student_info['age']

# Loops and built-in methods for dictionaries
# keys()
for k in student_info.keys():
    print(k)

# values()
for v in student_info.values():
    print(v)

#items()
for key, value in student_info.items():
    print(key, value)

# update() method
student_info.update({'patronum': 'stag'})

topics = ('Math', 'Grammar', 'History', 'Sport')
grades = [85, 90, 100, 75]
print(dict(zip(topics, grades)))