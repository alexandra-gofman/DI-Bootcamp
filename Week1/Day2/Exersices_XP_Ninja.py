#Ex_4
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))

#Ex_5
number_of_loops = 5
len_of_the_longest_sentence = 0
for i in range(number_of_loops):
    user_word = input('Your sentense without A: ')
    if 'a' not in user_word and 'A' not in user_word:
        if len(user_word) > len_of_the_longest_sentence:
            print('Your sentence without A is longest')
            len_of_the_longest_sentence = len(user_word)
        else:
            print('Your sentence without A is NOT longest')
    else:
        print('Found letter A in your sentence, please try again')

