from Ejercicio1 import *
from Ejercicio2 import *

def ejecutar():
    while True:
        opcion = input('Seleccione el ejercicio que desea ejecutar:\n1. Ejercicio_1\n2. Ejercicio_2\n')

        if opcion == '1':
            Ejercicio1.main()
            break
        elif opcion == '2':
            Ejercicio2.jugar()
            break
        else:
            print('Opción inválida. Intente de nuevo.')