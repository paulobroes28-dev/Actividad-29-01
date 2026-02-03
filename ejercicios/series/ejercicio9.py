def ejercicio_9():
    print("Rendimiento de inversión.")
    cantidad = float(input("Cantidad a invertir: "))
    interes = float(input("Interés anual: "))
    años = int(input("Número de años: "))

    for i in range(años):
        vf=cantidad*(1 + interes)
        print("Año", i+1, ": Capital acumulado", vf)