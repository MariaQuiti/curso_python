print("======Trabajando con diccionarios=====")

empty_dict = {}

fullfiled_dict = {
    "id": 1,
    "color": "azul"
}

print(empty_dict, fullfiled_dict)

lista_1 = ["a1", "b2"]
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1, dict(tupla_1))

list_dimensional = [['a', 1], ['b', 3]]
print(list_dimensional, dict(list_dimensional))

#añadir un elemento a diccionario
dictionary = {'A': 1, 'B': 2, 'C': 3}
key, value = 'D', 4

dictionary.update({key: value})
print(dictionary)

#obtener un elemento
dictionary = {'A': 1, 'B': 2, 'C': 3}
obtener_elemento = dictionary['B']
print(obtener_elemento)

#modificar un elemento
key, value = 'C', 4
dictionary.update({key: value})
print(dictionary)

#eliminar un elemento
del dictionary['B']
print(dictionary)

empty_dict_2 = dict()
print(empty_dict_2)

full_dict = dict(
    genero = "F",
    nacionalidad = "C" 
)

print(full_dict)

empleado = {
    "name": "hello",
    "apellido": "kitty"
}

print(empleado)
for variablex in empleado.values():
    print(variablex)


print("===== Trabajando con condicionales =====")

# if
edad = 60
if edad > 50:
    print("Hola micky mouse")
    print("print if")

print("fuera del if")

#if, else:
temperatura = 38
if temperatura >= 37:
    print("tienes fiebre")
else:
    print ("la temperatura aun es normal")


sismo = 8
pais = 'Chile'

if sismo > 6:
    if pais == 'Chile':
        print('los edificios no se caerán')
    else:
        print('los edificios se caeran')
else:
    if pais == 'Chile':
        print('nose')
    else:
        print('otro')

#Escriba un programa que permita adivinar un personaje de Marvel
#en base a estas tres preguntas


volar = False
humano = True
mascara = True

if volar == True:
    if humano == True:
        if mascara == True:
            print('Hombre Pájaro')
        else:
            print('Superman')
    else:
        if mascara == True:
            print('Homero Simpson')
        else:
            print('Bety la fea')
else:
    if humano == True:
        if mascara == True:
            print('Spiderman')
        else:
            print('El gato con botas')
    else:
        if mascara == True:
            print('Micky Mouse')
        else:
            print('Sherk')


print("======Trabajando con ciclos, While 1=======")

want_exit = 'n'
while want_exit == 'n':
    print("hola cómo estás?")
    want_exit = input("¿Quieres salir? s/n")
print("fuera del while")

print("======Trabajando con ciclos, While 2=======")
#break nos permite romper un ciclo

want_exit = 'n'
num_questions = 0
while want_exit == 'n':
    print("Hola como estas?")
    want_exit = input("Quieres salid? S/N")
    num_questions += 1
    if num_questions == 4:
        print("Alcanzaste el máximo permitido?")
        break
print("se acabó el while")