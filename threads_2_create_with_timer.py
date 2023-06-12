""""
    Author: Reyes Gonzalez Agustin Oscar
    Created at: 07/June/2023
    
    En este archivo se muestran diferentes formas de crear hilos con temperalizador.
"""

import threading

#Funcion a ejecutar con los hilos.
def info():
    print(f"ID: {threading.get_native_id()}")
    

#Se crea hilo que se ejecuta despues de 5 segundos.
temporalizer_thread = threading.Timer(5, function=info)
temporalizer_thread.start()