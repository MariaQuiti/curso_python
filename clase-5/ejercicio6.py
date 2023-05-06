#6. Se le asignado un tarea para programar un algoritmo para una lavadora, debe investigar 
#cuanta agua se neceita para lavar prendas con las siguientes caracteriticas, 
# algodon, nilon, poliester, debe investigar para una lavadora de xx kg cuantas prendas de cada una puede 
# lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente.
#Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14,
# entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.
#
#    Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#    La función aceptará 2 argumentos: - carga lavadora y ropa.

def lavadora(carga_lavadora, cantidad_ropa, tipo_tela):
    factores_agua = {
        "algodon": 5,
        "nilon": 3,
        "poliester": 2
    }

    factor_agua = factores_agua.get(tipo_tela.lower(), 1)

    cantidad_agua = factor_agua * (1.1 ** (cantidad_ropa - carga_lavadora))

    print(cantidad_agua)

lavadora()