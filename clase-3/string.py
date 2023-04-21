firs_name = "María"
last_name = "Bravo"
print(firs_name + "_" + last_name)

mensaje1 = "gatito " * 3
print(mensaje1)

mensaje2 = "gato"
print(mensaje2)
mensaje2 += " con botas"
print(mensaje2)

print(len(mensaje2))

cadena = "debo mantenerme sereno para no caer en la locura"
position = cadena.find("gato")
print("gato se encuentra en: ", position)
position = cadena.find("locura")
print("locura se encuentra en: ", position)

hola = 'SHERK Y BURRO'
hola_lower = hola.lower()
print(hola)
print(hola_lower)


x = hola.replace("BURRO","GATO")
print(x)


print("======= Listas =======")

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 455, 7.6, [2,"a"], {"name": "Quit"}]
print(fullfiled_list)

second_list = list()
print(second_list)

print(list("Concurso"))

range_one = range(50)
print(list(range_one))

numero = [1, 4, 6, 10]
print(numero)
numero.append(10,)
print(numero)

print(numero[2])

x = ["a", "b", "c", "d"]

x.remove("c")
print(x)

x[1] = "r"
x[2:] = ["s", "t"]
print(x)

print ("====tuplas====")

empty_tuple = ()
fullfiled_tuple = (1, "quiti", 500.87)

print(empty_tuple, fullfiled_tuple)

print(type(fullfiled_tuple))

one_tuple = ('Mariana',)
print(type(one_tuple))

reverse(fullfiled_tuple)