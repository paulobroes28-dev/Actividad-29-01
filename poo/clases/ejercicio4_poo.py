class Ejercicio4:
    def __init__(self):
        self.f = 0
        self.c = 0
    def leer_datos(self):
        print("Programa que convierte grados.")
        self.f=int(input("Grados Farenheit= "))
    def calcular(self):
        self.c=(self.f-32)*5/9
    def mostrar_resultados(self):
        print("Grados Centígrados= ",self.c)