class Ejercicio8:
    def __init__(self):
        self.num = 0

    def leer_datos(self):
        print("Programa que muestra números impares.")
        self.num = int(input("Ingrese un número entero positivo: "))

    def calcular(self):
        pass

    def mostrar_resultados(self):
        for i in range(1, self.num+1, 2):
            print(i, end=", ")