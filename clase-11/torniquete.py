class Torniquete:
    pasajeros = []

    def __init__(self, fecha, patente):
        self.fecha = fecha
        self.patente = patente
        self.contador_pasajeros = 0
        self.saldo = 0
        
    
    def agregar_pasajero(self):
        self.pasajeros.append({
            'adulto' : 730,
            'adulto_mayor' : 365,
            'niño' : 0
        })

    def giro_torniquete(self, pasajeros):
        if pasajeros == 'adulto':
            self.contador_pasajeros += 1
            self.saldo += 730
            print(f'Ha pasado por el torniquete un {pasajeros}')
        elif pasajeros == 'adulto_mayor':
            self.contador_pasajeros += 1
            self.saldo += 365
            print(f'Ha pasado por el torniquete un {pasajeros}')
        elif pasajeros == 'niño':
            self.contador_pasajeros += 1
            print(f'Ha pasado por el torniquete un {pasajeros}')
        else:
            print("Por favor ingrese un tipo de pasajero que sea adulto, adulto_mayor o niño")

    def reporte_operacion(self):
        print(f'\n *******Reporte de operaciones transporte {self.patente}******** \n')
        print(f'El transporte ha recaudado $ {self.saldo}')
        print(f'Han ingresado {self.contador_pasajeros} personas')


micro = Torniquete('22/may/2023', 'XCXP43')


micro.agregar_pasajero()

# Paso por torniquete de pasajeros
micro.giro_torniquete('adulto')
micro.giro_torniquete('adulto_mayor')
micro.giro_torniquete('niño')
micro.giro_torniquete('adulto')
micro.giro_torniquete('adulto')
micro.reporte_operacion()



       