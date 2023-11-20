from models.animal import Animal

class Pet(Animal):
    animal_type = ''
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)

    
    def __str__(self) -> str:
        return super().__str__() + f', {self.animal_type}'
    
class Dog(Pet):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Dog'


class Cat(Pet):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Cat'


class Hamster(Pet):
    def __init__(self, name, commands, birthdate):
        super().__init__(name, commands, birthdate)
        self.animal_type = 'Hamster'
