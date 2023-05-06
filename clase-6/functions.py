def greet(name):
    print(f'Hola {name} :)')

greet('perro')
greet('gato')

def greet_two(first_name, last_name):
    print(f'Hola {first_name} {last_name} :)')

greet_two(last_name = 'con botas', first_name = 'gato')

def multiplicar_text(text, multiplier = 2):
    print(text * multiplier)

multiplicar_text("V", 5)
multiplicar_text("X")

def varietal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

print("\n==========\n")
varietal("1a", "2b", 0, "xx", [0, 1])

def varietal_dos(param1, **others):
    print(param1)
    print(others)

varietal_dos("1a", id = 0, name = 'Mati')