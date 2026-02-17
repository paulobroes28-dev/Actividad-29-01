class Ejercicio5:
    def __init__(self):
        self.g = 0
        self.L = 0
    def leer_datos(self):
        print("Programa que permite convertir.")
        self.g=int(input("galones= "))
    def calcular(self):
        self.L=self.g*3.7854
    def mostrar_resultados(self):     
        print("litros= ",self.L)