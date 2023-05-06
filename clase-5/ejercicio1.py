# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra
# asociada con esa calificación. con al siguiente tabla
#    0   - 2     D
#    2.1 - 5     C
#    5.1 - 6     B
#    6.1 - 7     A

nota1 = 4.5
nota2 = 5.3
nota3 = 1

promedio = ((nota1 + nota2 + nota3)/3)

if promedio <= 2:
    print("Tu calificación es D")
elif promedio >= 2.1 and promedio <= 5:
    print("Tu calificación es C")
elif promedio >= 5.1 and promedio <= 6:
    print("Tu calificación es B")
elif promedio >= 6.1 and promedio <= 7:
    print("Tu promedio es igual a A")
else:
    print("Creo que hubo un error, porfavor introduce notas entre 0 y 7")



