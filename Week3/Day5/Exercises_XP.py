import os
import random
import json
import datetime

# Ex_1
def get_words_from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}\words.txt', 'r', encoding='utf-8') as file_obj:
        file_content = file_obj.read()
    file_content_list = list(file_content.split('\n'))
    return file_content_list

def get_random_sentence(length):
    file_content_list = get_words_from_file()
    sentence = ''
    for i in range(length):
        ind_in_list = random.randint(0, len(file_content_list) - 1)
        sentence += f'{file_content_list[ind_in_list]} '
    sentence = sentence[:-1].lower() + '.'
    return sentence

def main():
    print('This program can crate a sentence with words from words.txt with length user chooses.')
    length = input('Please enter the length of sentence you want to get: ')
    try:
        length = int(length.strip())
        if 2 <= length <= 20:
            return get_random_sentence(length)
        else:
            raise Exception('Choose a number in range [2,20]')
    except ValueError:
        return 'Your input is not an integer.'


print(main())

#Ex_2

sampleJson =''' {
   "company":{ 
      "employee":{ 
         "name":"emma",
         "birth_date":"YYYY-MM-DD",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}'''
json_content = json.loads(sampleJson)
print(json_content["company"]["employee"]["payable"]["salary"])
json_content["company"]["employee"]["birth_date"] = datetime.datetime.today().strftime('%Y-%m-%d')

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}\employee.json', 'w') as f:
    json.dump(json_content, f, indent=4)