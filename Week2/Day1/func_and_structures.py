#FUNCTIONS AND DATA SRTUCTURES

students = ['Harry', 'Ron', 'Hermione']

#create a func that says 'Name, welcome to Hogwarts!' for each one of the students of the given list

def greetings() -> str:
    for name in students:
        print(f'{name}, welcome to Hogwarts!')

greetings()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - Gryffindor'

get_house()
print(students)