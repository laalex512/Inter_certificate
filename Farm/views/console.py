from models.animal import *
from models.pet import *
from models.working_animal import *
import database as db


COUNT_ATTEMPTS = 3
MENU = "\n1 - View all animals\n\
2 - Add new animal\n\
3 - View animal commands\n\
4 - Learn new command\n\
q - Quit\n\
Enter: "


def password_request():
    password_counter = 0
    while password_counter < COUNT_ATTEMPTS:
        input_pass = input("Enter password to enter to db: ")
        if input_pass != db.PASSWORD:
            password_counter += 1
            continue
        else:
            return True
    return False


def get_animal_types():
    result = []
    for sub_class in Pet.__subclasses__():
        result.append(sub_class.__name__)
    for sub_class in WorkingAnimal.__subclasses__():
        result.append(sub_class.__name__)
    return result


def find_animal_by_name():
    name = input("Name: ").capitalize()
    find_animal_list = []
    for animal in db.output_all_animals():
        if animal.name == name:
            find_animal_list.append(animal)
    match len(find_animal_list):
        case 0:
            return None
        case 1:
            return find_animal_list[0]
        case _:
            message = f'We find {len(find_animal_list)} animals with name {name}, Choose which one:\n'
            for i in range(1, len(find_animal_list) + 1):
                message += f'{i} - {find_animal_list[i-1]}\n'
            animal_number = int(input(message))
            return find_animal_list[animal_number - 1]


def user_request():
    if password_request():
        while True:
            user_input = input(MENU)
            match user_input:
                case 'q':
                    break
                case '1':
                    print(*db.output_all_animals(), sep='\n', end='\n')
                case '2':
                    animal_type = input(
                        f"Type {get_animal_types()} : ").capitalize()
                    if animal_type in get_animal_types():
                        name = input("Name: ").capitalize()
                        commands = input("Commands: ")
                        birthdate = input("Birthdate (YYYY-MM-DD) : ")
                        print(db.new_animal(db.create_animal(
                            name, commands, birthdate, animal_type)))
                    else:
                        print("This animal type doesn't exist")
                case '3':
                    finding_animal = find_animal_by_name()
                    if finding_animal:
                        print(finding_animal.commands)
                    else:
                        print(f"Animal with name {name} doesn't exist")
                case '4':
                    finding_animal = find_animal_by_name()
                    if finding_animal:
                        new_command = input("Enter new command: ")
                        db.learn_command(finding_animal, new_command)
                        print("Command successfully learned")
                    else:
                        print(f"Animal with name {name} doesn't exist")
                case _:
                    print("Enter correct menu item")
