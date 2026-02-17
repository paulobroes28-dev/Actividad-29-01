class Ejercicio6:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.distancia = 0

    def leer_datos(self):
        print("Programa que calcula la distancia.")
        self.num1=float(input("Escriba un número: "))
        self.num2=float(input("Escriba otro número: "))

    def calcular(self):
        if self.num1>self.num2:
            self.distancia=self.num1-self.num2
        else:
            self.distancia=self.num2-self.num1

    def mostrar_resultados(self):
        print("La distancia entre",self.num1,"y",self.num2,"es",self.distancia)