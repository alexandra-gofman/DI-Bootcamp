import random

#Ex_1

def display_message():
    print('I am learning about functions in Python.')

display_message()

#Ex_2

def favorite_book(title):
    return f'One of my favorite books is {title}'

print(favorite_book('Alice in Wonderland'))

#Ex_3

def describe_city(city, country = 'Unknown'):
    return f'{city} is in {country}'

print(describe_city('Paris'))

#Ex_4

def number_compare(number:int):
    if not 1 <= number <= 100:
        raise ValueError('Number must be from 1 to 100')
    new_number = random.randint(1, 100)
    if number == new_number:
        return 'Success!'
    else:
        return f'Fail! Your number: {number}, Random number: {new_number}'


print(number_compare(45))

#Ex_5

def make_shirt(size = 'large', text = 'I love Python'):
    return f'The size of the shirt is {size} and the text is {text}.'

print(make_shirt())
print(make_shirt('medium'))
print(make_shirt(text='different message'))
print(make_shirt(size="small", text="Hello!"))

#Ex_6


def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    for i, magician in enumerate(magician_names):
        magician_names[i] = magician + ' the Great'
    return magician_names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
make_great(magician_names)
show_magicians(magician_names)

#Ex_7
def get_random_temp():
    return random.uniform(-10, 40)

def main():
    temperature = get_random_temp()
    print(f'The temperature right now is {temperature} degrees Celsius.')

    if temperature < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif 0 <= temperature <= 16:
        print('Quite chilly! Don’t forget your coat.')
    elif 16 < temperature <= 23:
        print('Nice weather.')
    elif 23 < temperature <= 32:
        print('A bit warm, stay hydrated.')
    elif 32 < temperature <= 40:
        print('It’s really hot! Stay cool.')

main()

