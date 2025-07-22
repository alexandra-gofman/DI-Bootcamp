#DATA STRUCTURES: SEQUENCES

#TUPLES: UMMUTABLE
my_tuple = (1324)

nums = [1, 2, 34, 5, 67]
nums_tuple = tuple(nums)
print(nums_tuple)

#tuples methods
cities = ('NY', 'BO', 'SP', 'RJ', 'NY')
print(cities.count('NY'))
print(cities[1])
print(cities.index('SP'))

#unpacking
languages = ('EN', 'RU', 'JP', 'HE')
lang1, lang2, lang3, lang4 = languages
print(lang1)

#SETS
#UNORDERED, CANT BE 2 SAME ELEMENTS, CAN BE DIFFERENT DATA TYPR IN ONE SET

some_set = set()
other_set = {1, 2, 6}

countries = {'Israel', 'US', 'Brazil'}
names = {'Shimon', 'Israel', 'David'}

set_3 = countries.intersection(names)
print(set_3)

merged_set = countries.union(names)
print(merged_set)

dif_set = countries.difference(names)
print(dif_set)