#1
a = [1, 2, 3, 4]
for num in a:
    print(num)

#2
a = [1, 2, 3, 4]
for num in a:
    print(num * 20)

#3
a = ["Elie", "Tim", "Matt"]
new_a = []
for name in a:
    new_a.append(name[0])
print(new_a)

#4
a = [1, 2, 3, 4, 5, 6]
for num in a:
    if num % 2 == 1:
        a.remove(num)
print(a)

#5
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []
for num in a:
    if (num in b) and (num not in c):
        c.append(num)
print(c)

#6
a = ["Elie", "Tim", "Matt"]
b = []
for word in a:
    reversed_word = word[::-1]
    b.append(reversed_word.lower())
print(b)

#7
a = 'first'
b = 'third'
c = ''
for letter in a:
    if letter in b and letter not in c:
        c = c + letter
print(list(c))

#8
a = []
for num in range(1, 101):
    if num % 12 == 0:
        a.append(num)
print(a)

#9
a = 'amazing'
vowels = 'aoeiu'
new_a = ''
for letter in a:
    if letter not in vowels:
        new_a = new_a + letter
print(list(new_a))

#10
b = []
for i in range(3):
    a = []
    for j in range(3):
        a.append(j)
    b.append(a)
print(b)

#11
b = []
for i in range(10):
    a = []
    for j in range(10):
        a.append(j)
    b.append(a)
print('[')
for line in b:
    print(f'{line},')
print(']')


