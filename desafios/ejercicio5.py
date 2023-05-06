print('***** Obtener Capital *****')
cantidad_invertir = float(input("Cuál es la cantidad a invertir? "))
interes_anual = float(input("Cuál es el porcentaje anual de interés? "))
num_anios = int(input("Cuántos años quiere invertir? "))

capital_obtenido = cantidad_invertir * (1 + (interes_anual/100))**num_anios

print("El capital obtenido es de:", round(capital_obtenido, 1), "Pesos")