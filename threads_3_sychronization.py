""""
    Author: Reyes Gonzalez Agustin Oscar
    Created at: 07/June/2023
    
    En este archivo se muestra cómo sincronizar hilos.
"""

from time import sleep
import threading
import random

#Función a ejecutar.
def info():
    print("Comineza ejecución")
    print(f"Hilo: {threading.current_thread().name}")
    sleep(random.random()) #Duerme el programa x segundos de manera aleatoria.
    print("Termina ejecución")

#Se crean los hilos a ejecutar.
thread1 = threading.Thread(target=info, name="Hilo 1")
thread2 = threading.Thread(target=info, name="Hilo 2")

#Se ejecutan los hilos.
thread1.start()
thread2.start()

#El programa principal espera hasta que terminen los hilos con el método join().
thread1.join()
thread2.join()

print("El hilo principal termina")