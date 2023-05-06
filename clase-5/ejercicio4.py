#4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#    Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
#    forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.



def trimestre():
    '''1-3, 4-6, 7-9, 10-12'''
    mes = int(input("ingrese número de mes entre 1 y 12"))

    if mes >= 1 and mes <=3:
        print("El mes número", mes, " corresponde al trimestre 1")
    elif mes >= 4 and mes <=6:
        print("El mes número", mes, " corresponde al trimestre 1")
    elif mes >= 7 and mes <=9:
        print("El mes número", mes, " corresponde al trimestre 1")
    elif mes >= 10 and mes <=12:
        print("El mes número", mes, " corresponde al trimestre 1")
    else:
        print("Ha ocurrido un error, ingrese un numero entre 1 y 12")

trimestre()
    