import math

def line():
    print("TO DO")
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente x1: "))
    x2 = float(input("Ingrese el coeficiente x2: "))

    print(f"El coeficiente A de su ecuación es: {A}")
    print(f"El coeficiente B de su ecuación es: {B}")
    print(f"El coeficiente x1 de su ecuación es: {x1}")
    print(f"El coeficiente x2 de su ecuación es: {x2}")

    print(f"\nPara la siguiente ecuación:")
    print(f"\tY = {A}x + {B}")

    Y1 = A * x1 + B
    Y2 = A * x2 + B

    print(f"\nDados los siguientes puntos:")
    print(f"\tP1 ({x1}, {Y1})")
    print(f"\tP2 ({x2}, {Y2})")

    Distancia = math.sqrt((x2 - x1)**2 + (Y2 - Y1)**2)
    print(f"\nLa distancia entre ellos es: {Distancia}")

line()

