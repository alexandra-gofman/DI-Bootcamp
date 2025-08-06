

class Farm:

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        '''Adding animals to the farm object's dict, with their type and number (attr. count)
        dict.key = animal_type
        dict.value = number of animals of this type
        it creates new key-value if it doesn't exist'''
        if animal_type in self.animals:
            self.animals[animal_type] += count
        elif animal_type not in self.animals:
            self.animals[animal_type] = count
        return self.animals

    def get_info(self):
        '''Output of object's animal dict and its name(info for user)'''
        animals_output = ''
        for key, value in self.animals.items():
            animals_output += f'{key} : {value} \n'
        return f'Farm {self.farm_name} has -\n{animals_output}E-I-E-I-0!'

    def get_animal_type(self):
        '''Taking only type of animals from object's animal dict, putting it into a list and sort it by letters'''
        list_of_animal_types = []
        for key in self.animals.keys():
            list_of_animal_types.append(key)
        list_of_animal_types.sort()
        return list_of_animal_types

    def get_short_info(self):
        '''Output of short info about farm (name and animals)
        if it's more than 1 animal of this type, adding 's' after type
        also checks if there are no animals on the farm and returns the info message'''
        output = f"{self.farm_name}'s farm has "
        if len(self.animals) > 0:
            list_of_animal_types = self.get_animal_type()
            for animal in list_of_animal_types:
                if self.animals[animal] < 1:
                    output += f"{animal}, "
                else:
                    output += f"{animal}s, "
            output = f'{output[:-2]}.'
        else:
            output += 'no animals.'
        return output

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_type())
print(macdonald.get_short_info())