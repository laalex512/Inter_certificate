class Animal:

    def __init__(self, name, commands, birthdate):
        self.name = name
        self.commands = commands
        self.birthdate = birthdate

    def __str__(self) -> str:
        return f'Name: {self.name}, Commands: {self.commands}; Birthdate: {self.birthdate}'
