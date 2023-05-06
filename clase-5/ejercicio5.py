#5. Escriba un programa que eliminar un signo de exclamación del final de una cadena. 
#    puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

def eliminar_exclamacion():
    cadena = input("Ingrese la frase que desea modificar: ")
    eliminar = cadena[:-1].replace("!","")
    print(eliminar)

eliminar_exclamacion()