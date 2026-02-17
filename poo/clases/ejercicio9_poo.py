class Ejercicio9:
    def __init__(self):
        self.cantidad = 0
        self.interes = 0
        self.años = 0

    def leer_datos(self):
        print("Rendimiento de inversión.")
        self.cantidad = float(input("Cantidad a invertir: "))
        self.interes = float(input("Interés anual: "))
        self.años = int(input("Número de años: "))

    def calcular(self):
        for i in range(self.años):
            vf=self.cantidad*(1 + self.interes)
    def mostrar_resultados(self):
        for i in range(self.años):
            vf=self.cantidad*(1 + self.interes)
            print("Año", i+1, ": Capital acumulado", vf)
