import string
import random
from datetime import datetime
from faker import Faker

#Ex_1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f'1 {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        if self.amount == 1:
            return f'1 {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError('Cannot add between Currency type <dollar> and <shekel>')
            new_obj = Currency(self.currency, self.amount + other.amount)
            return new_obj
        elif isinstance(other, int):
            return self.amount + other

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError('Cannot add between Currency type <dollar> and <shekel>')
            self.amount += other.amount
            return self
        elif isinstance(other, int):
            self.amount += other
            return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'
#
print(c1 + 5)
# 10
#
print(c1 + c2)
# 15
#
print(c1)
# 5 dollars
#
c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars
#
# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>

#Ex_3

output = ''
for i in range(5):
    new_letter_ind = random.randint(0, len(string.ascii_letters) - 1)
    output += string.ascii_letters[new_letter_ind]
print(output)

#Ex_4

print(datetime.today().date())

#Ex_5

date_now = datetime.today()

new_year_date = datetime(2026, 1, 1, 0, 0, 0, 0)

time_left = new_year_date - date_now

print(f'time left until January 1st \ndays: {time_left.days}, hours: {time_left.seconds // 3600}, minutes: {time_left.seconds % 3600 // 60}')

#Ex_6

birthday_date = input('Please enter your birtiday (YYYY/MM/DD): ')
birthday_date = datetime.strptime(birthday_date, '%Y/%m/%d')
date_now = datetime.today()
time_passed = date_now - birthday_date
print(f'{round(time_passed.total_seconds() / 60) } minutes passed from your birth')

#Ex_7

def add_user(number):
    users = []
    fake = Faker() #generator
    for i in range(number):
        new_user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code(),
        }
        users.append(new_user)
    return users


users = add_user(2)
print(users)