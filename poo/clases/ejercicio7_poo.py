class Ejercicio7:
    def __init__(self):
        self.palabra = ""

    def leer_datos(self):
        print("Programa que muestra una palabra 10 veces.")
        self.palabra = input("Ingrese una palabra: ")

    def calcular(self):
        pass

    def mostrar_resultados(self):
        for i in range(10):
            print(self.palabra)