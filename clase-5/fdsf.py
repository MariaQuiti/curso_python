mes = int(input("Ingrese el número de mes (1-12): "))

if mes >= 1 and mes <= 3:
    trimestre = 1
elif mes >= 4 and mes <= 6:
    trimestre = 2
elif mes >= 7 and mes <= 9:
    trimestre = 3
elif mes >= 10 and mes <= 12:
    trimestre = 4
else:
    print("El número de mes ingresado es inválido")

if mes >= 1 and mes <= 12:
    print("El mes", mes, "pertenece al trimestre", trimestre)