import random

#Ex_1

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):

    def __init__(self, name, age, eye_color, talkative):
        super().__init__(name, age)
        self.eye_color = eye_color
        self.talkative = talkative

    def meow(self):
        return f'meow!' * self.talkative

cat1 = Bengal('Lola', 2)
cat2 = Chartreux('Tiny', 7)
cat3 = Siamese('Rokky', 5, 'blue', 3)
all_cats = [cat1, cat2, cat3]

sara_pets = Pets(all_cats)
sara_pets.walk()

#Ex_2

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f'{self. name} won the fight'
        else:
            return f'{other_dog.name} won the fight'

dog1 = Dog('Lucky', 4, 12)
dog2 = Dog('Rex', 8, 20)
dog3 = Dog('Zoe', 1, 2)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

#Ex_3

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f'{self. name} won the fight'
        else:
            return f'{other_dog.name} won the fight'

class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.trained = True
        print(self.bark())
        return

    def play(self, *args):
        dogs = ''
        for i, dog in enumerate(args):
            if i != len(args) - 1:
                dogs += f'{dog.name}, '
            else:
                dogs += f'{dog.name} '
        dogs += f'play together.'

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.do_a_trick()


#Ex_4

class Person:

    def __init__(self, first_name, age, last_name=''):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)

    def check_majority(self, first_name):
        for i, member in enumerate(self.members):
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f'There is no person with name {first_name}')


    def family_presentation(self):
        print(f'Family`s last name: {self.last_name}')
        for member in self.members:
            print(f'Name: {member.first_name}  Age: {member.age}')

family = Family("Cohen")

family.born("David", 20)
family.born("Sara", 16)

family.check_majority("David")
family.check_majority("Sara")
family.check_majority("John")

family.family_presentation()




