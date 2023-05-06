num1 = 80
num2 = 5
num3 = 8

if num1 >= num2:
    if num2 >= num3:
        print(f'{num1} es mayor que {num2} es mayor que {num3}')
    else:
        if num1 >= num3:
            print(f'{num1} es mayor que {num3} es mayor que {num2}')
        else:
            print(f'{num3} es mayor que {num1} es mayor que {num2}')
elif num2 >= num1:
    if num1 >= num3:
        print(f'{num2} es mayor que {num1} es mayor que {num3}')
    else:
        if num2 >= num3:
            print(f'{num2} es mayor que {num3} es mayor que {num1}')
        else:
            print(f'{num3} es mayor que {num2} es mayor que {num1}')

