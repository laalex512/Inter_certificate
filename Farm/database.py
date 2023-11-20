from mysql.connector import connect, Error
from models.animal import Animal
from models.pet import *
from models.working_animal import *


HOST = "localhost"
USER = "root"
PASSWORD = "1"


def read_animals_types(cursor):
    """
    Возвращает словарь, в котором ключи - названия типа животного, значения - ID типа
    """

    read_types = """SELECT * FROM `animal_type`"""
    cursor.execute(read_types)
    types_dict = {}
    for row in cursor.fetchall():
        types_dict[row[1]] = row[0]
    return types_dict


def create_animal(name, commands, birthdate, animal_type):
    """
    Возвращает экземпляр соответствующего anymal_type класса животного
    """

    animal_class = globals()[animal_type]
    return animal_class(name, commands, birthdate)


def output_all_animals():
    """
    Возвращает список всех животных в питомнике в виде экземпляров соответствующих классов
    """
    try:
        result = []
        with connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        ) as connection:
            use_base = """USE man_friends"""
            read_animals = ''
            with connection.cursor() as cursor:
                cursor.execute(use_base)
                types_dict = read_animals_types(cursor)
                for item in types_dict.keys():
                    read_animals += f"""SELECT name, commands, birthdate, animal_type.title FROM {item.lower()} JOIN animal_type ON {item.lower()}.animal_type_id=animal_type.id UNION\n"""
                cursor.execute(read_animals[:-6])  # минус последний UNION
                for row in cursor.fetchall():
                    result.append(create_animal(*row))
                connection.commit()
        return result
    except Error as e:
        return (e)


def new_animal(animal: Animal):
    """
    Заносит в базу данных новое переданное животное
    """
    try:
        with connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        ) as connection:
            use_base = """USE man_friends"""
            with connection.cursor() as cursor:
                cursor.execute(use_base)
                types_dict = read_animals_types(cursor)
                animal_type_id = types_dict[animal.animal_type]
                table_name = animal.animal_type.lower()
                animal_save = f"""INSERT INTO {table_name} (animal_type_id, name, commands, birthdate) VALUES 
                ({animal_type_id}, "{animal.name}", "{animal.commands}", "{animal.birthdate}");
                """
                cursor.execute(animal_save)
                connection.commit()
        return f'{animal} added in database successfully'
    except Error as e:
        return (e)


def learn_command(animal: Animal, new_command: str):
    """
    Добавляет к переданному животному в базе данных новую команду
    """
    try:
        animal.commands += f', {new_command}'
        with connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        ) as connection:
            use_base = """USE man_friends"""
            with connection.cursor() as cursor:
                cursor.execute(use_base)
                table_name = animal.animal_type.lower()
                command_save = f"""UPDATE {table_name} SET commands = "{animal.commands}" WHERE name = "{animal.name}" AND birthdate = "{animal.birthdate}";
                """
                cursor.execute(command_save)
                connection.commit()
                return f'Command added successfully'
    except Error as e:
        return (e)
