print('******Calcular Salario******')
horas_trabajadas = float(input("Cuantas horas haz trabajado? "))
costo_hora = float(input("Cuanto es el costo por cada hora? "))

salario = horas_trabajadas * costo_hora
print(f'La paga que te corresponde es {salario} pesos')