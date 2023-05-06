
nombre = str(input("Ingrese su nombre: "))
sexo = str(input("Ingrese su sexo (M/H): "))

# if sexo == 'mujer':
#     if nombre < 'm':
#         print("Pertenece al grupo A")
#     else:
#         print("Pertenece al grupo B")
# else:
#     if nombre > 'n':
#         print("Pertenece al grupo A")

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f'Tu nombre es {nombre}, tu sexo es {sexo}, entonces perteneces al grupo {grupo}')
