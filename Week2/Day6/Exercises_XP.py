#Ex_1

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def find_the_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age:
        if cat1.age > cat3.age:
            return cat1
        elif cat1.age < cat3.age:
            return cat3
    elif cat1.age < cat2.age:
        if cat2.age > cat3.age:
            return cat2
        else:
            return cat3



cat1 = Cat('Fluffy', 10)
cat2 = Cat("Garfield", 5)
cat3 = Cat('Joe', 1)

the_oldest_cat = find_the_oldest_cat(cat1, cat2, cat3)

print(f'The oldest cat is {the_oldest_cat.name}, and is {the_oldest_cat.age} years old')

#Ex_2

class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2 } cm high!')

davids_dog = Dog('Rex', 35)

sarahs_dog = Dog('Lucky', 52)

print(f'{davids_dog.name} has {davids_dog.height} cm height')
davids_dog.bark()
davids_dog.jump()

print(f'{sarahs_dog.name} has {sarahs_dog.height} cm height')
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} taller than {sarahs_dog.name}')
elif sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} taller than {davids_dog.name}')
else:
    print(f'{davids_dog.name} and {sarahs_dog.name} have the same height')


#Ex_3

class Song:

    def __init__(self, lyrics:list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


#Ex_4

class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animals_dict = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print('This animal is already exists in the zoo')
        return

    def get_animals(self):
        print(self.animals)
        return

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f'{animal_sold} is not in the zoo')

    def sort_animals(self):
        self.animals.sort()
        for i, animal in enumerate(self.animals):
            self.animals[i] = animal.title()
            first_letter = animal[0]
            if first_letter in self.animals_dict.keys():
                self.animals_dict[first_letter].append(animal)
            else:
                self.animals_dict[first_letter] = list()
                self.animals_dict[first_letter].append(animal)

        return

    def get_groups(self):
        for key, value in self.animals_dict.items():
            print(f'{key}: {value}')
        return


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()


