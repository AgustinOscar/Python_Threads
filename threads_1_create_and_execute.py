""""
    Author: Reyes Gonzalez Agustin Oscar
    Created at: 07/June/2023
    
    En este archivo se muestran diferentes formas de instanciar y ejecutar un hilo.
"""

import threading

#Funcion a ejecutar con los hilos.
def math_operation(num1=10, num2=5, option="suma"):
    if option == "suma":
        result = num1 + num2
    elif option == "resta":
        result = num1 - num2
    elif option == "multiplicacion":
        result = num1 * num2
    else:
        result = num1 / num2
        
    #Se muestran en pantalla los datos del hilo.
    print("------------------------------------------------------------------------")
    print(f"Nombre: {threading.current_thread().name}")
    print(f"ID: {threading.get_native_id()}")
    print(f"Operacion:  {option}")
    print(f"Resultado: {result}")


#Forma 1 (SUMA) 
thread1 = threading.Thread(target=math_operation) 

#Forma 2 (RESTA)
thread2 = threading.Thread(target=math_operation, args=(80, 4, "resta"))

#Forma 3 (MULTIPLICACION)
thread3 = threading.Thread(target=math_operation, kwargs={"num1": 45, "num2": 2, "option":"multiplicacion" })

#Forma 4 (DIVISION)
thread4 = threading.Thread(target=math_operation, args=(100, 10, "division"), name="hilo de la division")


#Se ejecutan todos los hilos.
thread1.start()
thread2.start()
thread3.start()
thread4.start()