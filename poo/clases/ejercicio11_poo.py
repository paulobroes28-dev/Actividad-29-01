class Ejercicio11:
    def __init__(self):
        self.num = 0
        self.series = []

    def leer_datos(self):
        self.num = int(input("Ingrese un número para la serie Fibonacci: "))

    def calcular(self):
        a, b = 0, 1
        while a <= self.num:
            self.series.append(a)
            a, b = b, a + b

    def mostrar_resultados(self):
        print("Serie Fibonacci hasta el número", self.num, ":", self.series)