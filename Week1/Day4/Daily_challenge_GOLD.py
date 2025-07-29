from datetime import date

date_today = date.today()
user_date = input('Please write your birthday YYYY/MM/DD ')
user_date = user_date[-11:].replace(' ', '')
list_of_user_date = user_date.split('/')
birthday_date = date(int(list_of_user_date[0]), int(list_of_user_date[1]), int(list_of_user_date[2]))

birthday_was_in_this_year = False
if birthday_date.month < date_today.month and birthday_date.day < date_today.day:
    birthday_was_in_this_year = True

candles = date_today.year - birthday_date.year
if candles == 0:
    print('it`s a newborn!')
if birthday_was_in_this_year is False:
    candles -= 1

candles = candles % 10
num_underscores = 11 - candles

is_it_a_leap_year = False
if birthday_date.year % 400 == 0:
    is_it_a_leap_year = True
elif birthday_date.year % 100 == 0:
    is_it_a_leap_year = False
elif birthday_date.year % 4 == 0:
    is_it_a_leap_year = True


print(f'''       {(num_underscores // 2 )* "_"}{candles * "i"}{(num_underscores // 2) * "_"}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~''')


if is_it_a_leap_year is True:
    print(f'''        {(num_underscores // 2 )* "_"}{candles * "i"}{(num_underscores // 2) * "_"}
       |:H:a:p:p:y:|
     __|___________|__
    |^^^^^^^^^^^^^^^^^|
    |:B:i:r:t:h:d:a:y:|
    |                 |
    ~~~~~~~~~~~~~~~~~~~''')