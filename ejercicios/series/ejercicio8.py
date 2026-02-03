def ejercicio_8():
    print("Programa que muestra números impares.")
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num+1, 2):
        print(i, end=", ")