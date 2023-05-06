class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


perro = Animal('Dalmata', 'Grande')
print(perro.type)
perro.type = 'Chiquito'
print(perro.type)

print('\n ***************** \n')

class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid('arthur')

print(android.name)
android.name = 'robotito'
print(android.name)

android.hidden_name = 'Red'
print(android.hidden_name)
print(android.name)


print('\n ***************** \n')

class CalculatedValue:
    def __init__(self, _name, _height):
        self.name = _name
        self.height = _height

    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height
    
valuex = CalculatedValue("ratio", 10)

print(f'El {valuex.name} es: {valuex.get_calculate_value}')