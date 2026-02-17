class Ejercicio3:
    def __init__(self):
        self.m = 0
        self.km = 0

    def leer_datos(self):
        print("Programa de conversión.")
        self.m=int(input("millas= "))

    def calcular(self):
        self.km=self.m*1.609344

    def mostrar_resultados(self):
        print("km= ",self.km)