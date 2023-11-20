from models.animal import Animal


class WorkingAnimal(Animal):
    animal_type = ''

    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)

    def __str__(self) -> str:
        return super().__str__() + f', {self.animal_type}'


class Horse(WorkingAnimal):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Horse'


class Camel(WorkingAnimal):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Camel'


class Donkey(WorkingAnimal):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Donkey'
