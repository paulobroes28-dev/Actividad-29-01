import math
class Ejercicio2:
    def __init__(self):
        self.r = 0
        self.c = 0

    def leer_datos(self):
        self.r = int(input("r= "))

    def calcular(self):
        self.c = 2 * math.pi * self.r
    def mostrar_resultados(self):
        print("c= ", self.c)