from ejercicios.formulas.ejercicio1 import ejercicio_1
from ejercicios.formulas.ejercicio2 import ejercicio_2
from ejercicios.conversiones.ejercicio3 import ejercicio_3
from ejercicios.conversiones.ejercicio4 import ejercicio_4
from ejercicios.conversiones.ejercicio5 import ejercicio_5
from ejercicios.formulas.ejercicio6 import ejercicio_6
from ejercicios.series.ejercicio7 import ejercicio_7
from ejercicios.series.ejercicio8 import ejercicio_8
from ejercicios.series.ejercicio9 import ejercicio_9
from ejercicios.series.ejercicio10 import ejercicio_10
from ejercicios.series.ejercicio11 import ejercicio_11
from poo.clases.ejercicio1_poo import Ejercicio1
from poo.clases.ejercicio2_poo import Ejercicio2
from poo.clases.ejercicio3_poo import Ejercicio3
from poo.clases.ejercicio4_poo import Ejercicio4
from poo.clases.ejercicio5_poo import Ejercicio5
from poo.clases.ejercicio6_poo import Ejercicio6
from poo.clases.ejercicio7_poo import Ejercicio7
from poo.clases.ejercicio8_poo import Ejercicio8
from poo.clases.ejercicio9_poo import Ejercicio9
from poo.clases.ejercicio10_poo import Ejercicio10
from poo.clases.ejercicio11_poo import Ejercicio11

def menu_principal():
    while True:
        print("Menú principal")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("11. Ejercicio 11")
        print("12. Salir")
        op=int(input("Eliga una opción: "))
        match(op):
            case 1:
                #ejercicio_1()
                testp=Ejercicio1()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 2:
                #ejercicio_2()
                testp=Ejercicio2()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 3:
                #ejercicio_3()
                testp=Ejercicio3()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 4:
                #ejercicio_4()
                testp=Ejercicio4()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 5:
                #ejercicio_5()
                testp=Ejercicio5()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 6:
                #ejercicio_6()
                testp=Ejercicio6()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 7:
                #ejercicio_7()
                testp=Ejercicio7()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 8:
                #ejercicio_8()
                testp=Ejercicio8()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 9:
                #ejercicio_9()
                testp=Ejercicio9()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 10:
                #ejercicio_10()
                testp=Ejercicio10()
                testp.leer_datos() 
                testp.calcular()
                testp.mostrar_resultados()
            case 11:
                #ejercicio_11()
                testp=Ejercicio11()
                testp.leer_datos()
                testp.calcular()
                testp.mostrar_resultados()
            case 12:
                break
            case _:
                print("Opción no válida")