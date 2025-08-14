
import string

class Text:

    def __init__(self, text):
        self.text = text


    def word_frequency(self, word):
        text_list = self.text.split(' ')
        frequency = text_list.count(word)
        if frequency == 0:
            return f'There is no word {word} in the text'
        else:
            return frequency

    def most_common_word(self):
        text_list = self.text.split(' ')
        text_dict = {}
        for word in text_list:
            if word not in text_dict.keys():
                text_dict[word] = text_list.count(word)
        most_common_word = max(text_dict, key=text_dict.get)
        return most_common_word

    def unique_words(self):
        text_list = self.text.split(' ')
        unique_words = []
        for word in text_list:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        return cls(file_content)

class TextModification(Text):

    def remove_punctuation(self):
        punctuation = string.punctuation
        new_string = ''
        for char in self.text:
            if char not in punctuation:
                new_string += char
        return new_string

    def remove_stop_words(self):
        text_list = self.text.split(' ')
        stop_words = 'a, an, the, and, or, but, if, is, on, in, of, to, with, as, at, for, from, it, this, that, was, were, be, by, has, had, have'
        stop_words_list = stop_words.split(', ')
        new_text = ''
        for word in text_list:
            if word not in stop_words_list:
                new_text += word
        return new_text

    def remove_special_characters(self):
        regular_chars = string.ascii_letters + string.digits + ' '
        new_text = ''
        for char in self.text:
            if char in regular_chars:
                new_text += char
        return new_text



text = TextModification('qwerty^^^;;;; lol lol/ lo!l')
print(text.remove_special_characters())
