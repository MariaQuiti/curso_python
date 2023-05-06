class Organizacion_Nombres:
    def __init__(self):
        self.magia = ['Harry Houdini', 'David Blaine', 'Teller']
        self.cientificos = ['Newton', 'Hawking', 'Einstein']
        self.otros = ['Messi', 'Pele', 'Juanes']

    def hacer_grandioso(self):
        for i in range(len(self.magia)):
            self.magia[i] = 'El gran ' + self.magia[i]
    
    def imprimir_nombres(self):
        print("\n\n*****Lista completa de nombres*****")
        for nombre in self.magia + self.cientificos + self.otros:
            print(nombre)
        
        print("\n\n*****Nombres de los magos grandiosos*****")
        for nombre in self.magia:
            print(nombre)

        print("\n\n*****Nombres de los científicos*****")
        for nombre in self.cientificos:
            print(nombre)

        print("\n\n*****Otros nombres*****")
        for nombre in self.otros:
            print(nombre)


org_nombres = Organizacion_Nombres()
org_nombres.imprimir_nombres()
org_nombres.hacer_grandioso()
org_nombres.imprimir_nombres()
