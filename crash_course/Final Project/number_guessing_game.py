import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    #print(random_number)
    max_attempts = 7
    for i in range(max_attempts):
        a = int(input('Choose a number: '))
        if a < random_number:
            print('Too low!')
        elif a > random_number:
            print('Too high!')
        else:
            print('Congratulations! Your guess is correct!')
            return

    print(f'You lose. Correct answer is {random_number}')
    return


number_guessing_game()
