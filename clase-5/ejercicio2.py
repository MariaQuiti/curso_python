#2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#    Ejemplo whiole anidados:
#    while codicion1
#        while codicion2
#            .....

# Tabla de multiplicar a calcular
numero = 11

# Contador inicial para el ciclo
i = 1

# Ciclo while para imprimir la tabla de multiplicar del número indicado
while i <= 12:
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    i += 1
