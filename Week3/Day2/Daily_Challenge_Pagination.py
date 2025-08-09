import math

class Pagination:

    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items)/self.page_size)

    def get_visible_items(self):
        if len(self.items) > 0:
            first_item = self.page_size * self.current_idx
            last_item = first_item + self.page_size
            return self.items[first_item: last_item]
        if len(self.items) == 0:
            print('List of items is empty')


    def go_to_page(self,page_num):
        if 1 <= page_num <= self.total_pages:
            self.current_idx = page_num - 1
            return self
        else:
            raise ValueError('Page number is out of range')

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx != self.total_pages - 1:
            self.current_idx += 1
            return self
        else:
            print('You already on the last page')
            return self


    def previous_page(self):
        if self.current_idx != 0:
            self.current_idx -= 1
            return self
        else:
            print('You already on the first page')
            return self

    def __str__(self):
        items = self.get_visible_items()
        return str('\n'.join(items))


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

print(p.current_idx + 1)
# Output: 7
