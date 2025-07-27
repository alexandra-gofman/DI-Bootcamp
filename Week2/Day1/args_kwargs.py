#ARGS AND KWARGS
#ARGS = ARGUMENTS = LISTS, TUPLES, SETS
#KEY, WORD ARGUMENTS = DICTIONARIES


students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    print(args)
    if args:
        for name in args:
            print(f'{name}, welcome')
    else:
        print('you didn`t pass names')

welcome('Camila', 'Niv')

def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Juliana', email = 'aaaaaa@mail.com', is_online = True)