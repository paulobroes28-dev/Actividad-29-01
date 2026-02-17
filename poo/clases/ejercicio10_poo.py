class Ejercicio10:
    def __init__(self):
        self.num = 0

    def leer_datos(self):
        print("Programa que muestra un triángulo rectángulo.")
        self.num = int(input("Ingrese un número entero: "))

    def calcular(self):
        pass

    def mostrar_resultados(self):
        for i in range(1, self.num+1):
            print("0"*i)