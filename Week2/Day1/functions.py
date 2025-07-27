# FUNCTIONS

# A function is a reusable block of code that runs when you “call” it.

# Syntax

def func_name():
    '''prints a string in the console'''
    print('I am a function')

def func_hello():
    '''prints 'hello there' to the console'''
    print('hello there!')

func_name()
func_hello()

#Passing ARGUMENTS to the function
def greetings(language, name):
    '''print a greeting depending on language'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')
    elif language == 'ES':
        print(f'Hola {name}, que tal?')
    else:
        print('Unknown language')


greetings(name='Dolores', language='PT')

def multiply(calc) -> int:
    '''takes a number and multiply by 5'''
    result = calc * 5
    return result

print(multiply(3))

def country_info(country_name='Naboo') -> str:
    '''returns capital of given coutry'''
    if country_name == 'Naboo':
        return 'Theed'
    elif country_name == 'Russia':
        return 'Moscow'
    elif country_name == 'Israel':
        return 'Jerusalem'
    else:
        return 'Unknown country'

print(country_info('Israel'))

#Global and local Scope
age = 25

def current_age():
    print(age)
    my_age = 35
    my_age += 1

def happy_birthday():
    global age
    age += 1
    print(age)

current_age()
happy_birthday()