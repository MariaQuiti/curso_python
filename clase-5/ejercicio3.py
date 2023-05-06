#3. Escriba un programa que calcule el máximo común divisor 
#entre dos números enteros.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

num1 = 5
num2 = 15
resultado = mcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", resultado)