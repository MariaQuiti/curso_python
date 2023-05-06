#Creando una clase
class Transport:
    pass

#Instanciar la clase (llamarla) y crear un objeto
transport1 = Transport()
transport2 = Transport()

class PerroLipiGas:
    pass

lipi1 = PerroLipiGas()
lipi2 = PerroLipiGas()

print(type(transport1))
print(type(lipi1))

class Droid:
    def __init__(self):
        self.power_on = False

    def switch_on(self):
        print("Hola humana!")
        self.power_on = True
    
    def switch_off(self):
        print("Hasta la próxima amigos")
        self.power_on = False

androide1 = Droid()
androide2 = Droid()

androide1.switch_on()
androide2.switch_on()
print("power on 1: ", androide1.power_on)
print("power on 2: ", androide2.power_on)
androide1.switch_off()
print(androide1.power_on)


class Vehiculo:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehiculo('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehiculo('Pickup', 'Toyota')
print(pickup.type_vehicle, pickup.model_vehicle)