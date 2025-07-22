user_name = 'Alexandra'
email = 'alexandra@gmail.com'
user_age = 26
is_online = True

user_info = [user_name, email, user_age, is_online]
print(len(user_info))

some_list = list('item 1') #create a list
other_list = ['item 1', 'item 2']

print(some_list, other_list)

empty_list = []

print(user_info[2])

#slice
fruits = ['orange', 'kiwi', 'apple', 'lime']
print(fruits[-2:])

#LISTS ARE MUTABLE!
#STRINGS ARE NOT
fruits[2] = 'pineapple'
print(fruits)

#list methods
fruits = ['orange', 'kiwi', 'apple', 'lime']
fruits.insert(1, 'mango') #insert element with index = 1
print(fruits)

fruits.remove('kiwi') #removes the first apperance
print(fruits)

fruits.append('watermelon')
print(fruits)

fruits.pop() #delete the last one of the elemets
print(fruits)

fruits.pop(1) #delete element with index 1
print(fruits)

vegs = ['tomato', 'potato', 'carrot']
fruits.extend(vegs) #takes only one element
print(fruits)

#sorte() and .sort()
fruits_sorted = sorted(fruits)
print(fruits)
print(fruits_sorted)

fruits.sort()
print(fruits)


list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    i = list1.index(20)
    list1[i] = 200
print(list1)