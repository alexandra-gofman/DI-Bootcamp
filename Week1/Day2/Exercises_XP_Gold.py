#Ex_1
print("Hello world\n" * 4 + "I love python\n" *4)

#Ex_2
user_month = int(input('Write your month: '))
if user_month >= 3 and user_month <= 5:
    print('It\'s Spring!')
elif user_month >= 6 and user_month <= 8:
    print('It\'s Summer!')
elif user_month >= 9 and user_month <= 11:
    print('It\'s Autumn!')
else:
    print('It\'s Winter!')