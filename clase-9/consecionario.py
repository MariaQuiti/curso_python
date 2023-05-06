class Motocicleta:
    is_new = True
    motor = False

    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas,
                 _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso, _precio,
                 _combustible_maximo):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.precio = _precio
        self.combustible_maximo = _combustible_maximo

    def arrancar(self):
        if not self.motor:
            print('El motor ha arrancado')
        else:
            print('El motor ya estaba en marcha')

    def detener(self):
        if not self.motor:
            print('El motor ya estaba detenido')
        else:
            print('El motor se ha apagado')

    def consultar_precio(self):
        print(f'El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $')

    def consultar_combustible(self):

        print(f'\n***** Reporte del depósito de {self.marca} {self.modelo} Motocicleta *****')
        print(f'La cantidad de combustible es: {self.combustible_litros} litros')
        print(f'La capacidad máxima de combustible es: {self.combustible_maximo} litros')
        print(f'El espacio disponible en el deposito es: {self.combustible_maximo - self.combustible_litros} litros')
        print(f'                **********\n')

    def repostar(self):
        while True:
            self.repostar_litros = float(input("¿Cuantos litros desea repostar?:"))

            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print(f"Carga de combustible completada, ha cargado {self.repostar_litros} litros.")
                self.combustible_litros += self.repostar_litros
                print(f"Total combustible: {self.combustible_litros} litros \n")
                break
            else:
                print(f"La capacidad máxima son {self.combustible_maximo} litros, introduzca un número menor \n")


moto1 = Motocicleta('verde', 'xxcv45', 10, 2, 'Ousama', 'bojji', 2023/4/27, 50, 100, 9000, 17)  

moto2 = Motocicleta(
    _color = 'azul',
    _matricula = 'asdf45', 
    _combustible_litros = 0, 
    _numero_ruedas = 2,
    _marca = 'niq',
    _modelo = 'vespa',
    _fecha_fabricacion = 2023/4/27,
    _velocidad_punta = 50,
    _peso = 100,
    _precio = '', 
    _combustible_maximo = 20)

moto1.arrancar()
moto1.detener()
moto1.precio = 9000
print(f'El precio de la motocicleta {moto1.marca} {moto1.modelo} es de {moto1.precio} $')
moto1.consultar_precio()
moto1.consultar_combustible()
moto1.repostar()