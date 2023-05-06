print("***** Filtrando datos *****")
lista_personas = ['Harry Houdini', 'David Blaine', 'Teller', 'Newton', 'Hawking', 'Einstein', 'Messi', 'Pele', 'Juanes']

#separación por categorías
lista_magos = ['Harry Houdini', 'David Blaine', 'Teller']
lista_cientificos = ['Newton', 'Hawking', 'Einstein']
lista_otros = [
    nombre for nombre in lista_personas
        if nombre not in lista_magos and nombre not in lista_cientificos
]

def hacer_grandioso():
        for nombre in range(len(lista_magos)):
            lista_magos[nombre] = 'El gran ' + lista_magos[nombre]
            

def imprimir_nombres():
        print("\n***** Lista completa de nombres *****")
        for nombre in lista_personas:
            print(nombre)
        
        print("\n***** Nombres de los magos grandiosos *****")
        for nombre in lista_magos:
            print(nombre)

        print("\n***** Nombres de los científicos *****")
        for nombre in lista_cientificos:
            print(nombre)

        print("\n***** Otros nombres *****")
        for nombre in lista_otros:
            print(nombre)


hacer_grandioso()
imprimir_nombres()