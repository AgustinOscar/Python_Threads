import threading
import random

'''
# Esta es otra forma valida para utilizar el bloqueo.
def write_value(author, value):
    with lock_access_file:
        with open('results.txt', 'a') as file:  # abrimos el fichero para añadir contenido al final
            file.write(f'{author} - {value}\n')
'''


#Función que se ejecuta para escribir un valor en un fichero.
def write_value(author, value):
    lock_access_file.acquire() #Solicitud de acceso al recurso.
    with open('results.txt', 'a') as file:
        file.write(f'{author} - {value}\n')
    lock_access_file.release() #Se libera el recurso.

def function_to_execute():
    value = sum([random.random() for i in range(0, 100)])
    write_value(threading.current_thread().name, value)

# Se crea el objeto Lock.
lock_access_file = threading.Lock()

#Se crean los hilos.
thread1 = threading.Thread(target=function_to_execute, name="Hilo 1")
thread2 = threading.Thread(target=function_to_execute, name="Hilo 2")
thread3 = threading.Thread(target=function_to_execute, name="Hilo 3")
thread4 = threading.Thread(target=function_to_execute, name="Hilo 4")

#Se ejecutan los hilos.
thread1.start()
thread2.start()
thread3.start()
thread4.start()