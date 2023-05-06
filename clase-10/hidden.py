## Cree una clase llamada Artefacto, agregue tres atributos y 
## utilice los getter and setter para acceder a ellos.

class Artefacto:
    def __init__(self, name, color, type):
        self.__name = name
        self.__color = color
        self.__type = type

    @property
    def name(self) -> str:
         return self.__name
        
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        
    @property
    def color(self) -> str:
        return self.__color
        
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color
        
    @property 
    def type(self) -> str:
        return self.__type
        
    @type.setter
    def type(self, type: str) -> None:
        self.__type = type


microondas = Artefacto("Popi", "gris", "electrodomestico")
print(microondas.name)


class Empleado:
    sueldo_base = 100.000

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, _name):
        self.__name = _name

    @classmethod
    def obtener_sueldo_base(cls):
        return cls.sueldo_base
    
    @classmethod
    def modificar_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo


# Se desea automatizar el cajero de una entidad bancaria, para ellos se le ha encomendado
# realizar un programa en python a base de clases en la que se pueda crear una cuenta bancaria,
# registrar los movimientos de abono o cargo a la cuenta y además
# se debe pedir un estado de cuenta de la siguiente manera

# Movimiento#, Tipo Movimiento, Fecha Movimiento, Monto Movimiento, Saldo.