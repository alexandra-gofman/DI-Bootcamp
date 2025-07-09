#1
a = [("name", "Elie"), ("job", "Instructor")]
b = dict(a)
print(b)

#2
a = ["CA", "NJ", "RI"]
b = ["California", "New Jersey", "Rhode Island"]
c = {}
i = 0
for element in a:
    c[element] = b[i]
    i += 1
print(c)

#3
vowels = 'aoeiu'
a = {}
for letter in vowels:
    a[letter] = 0
print(a)

#4
a = []
b = []
for number in range(1, 27):
    a.append(number)
for letter in range(ord('A'), ord('Z') + 1):
    b.append(chr(letter))
print(dict(zip(a, b)))

#5 (Super Bonus)
a = 'awesome sauce'
vowels = 'aoeiu'
vowels = set(vowels)
b = dict.fromkeys(vowels, 0)
for letter in a:
    if letter in vowels:
        b[letter] += 1
print(b)


