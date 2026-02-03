def ejercicio_6():
    print("Programa que calcula la distancia.")
    num1=float(input("Escriba un número: "))
    num2=float(input("Escriba otro número: "))
    if num1>num2:
        distancia=num1-num2
    else:
        distancia=num2-num1
    print("La distancia entre",num1,"y",num2,"es",distancia)