import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def function_to_excecute(a, b):
    time.sleep(1)
    logging.info(f'Se realiza la tarea compleja con valores {a} y {b}.\n')

def greeting(name):
    logging.info(f'Saludo a {name}.\n')


#El hilo principal ejecuta la función.
function_to_excecute(5, 10)

#Se crea el pool de threads.
executor = ThreadPoolExecutor(max_workers=2) #Cuantos threads se van a crear.

#Llamando a la función a ejecutar.
executor.submit(function_to_excecute, 5, 20)
executor.submit(function_to_excecute, 7, 15) #Se ejecutan al mismo tiempo los dos hilos que hicieron la solicitud. 

executor.submit(function_to_excecute, 8, 48)
executor.submit(function_to_excecute, 1, 1) #Se ejecutan al mismo tiempo los siguientes dos hilos que hicieron la solicitud-

#Se pueden asignar tareas diferentes.
executor.submit(greeting, 'Agustín')
executor.submit(function_to_excecute, 8, 48) #Se ejecutan los dos últimos hilos al mismo tiempo.

#Se puede limitar el tiempo de vida de un pool de threads.
with ThreadPoolExecutor(max_workers=2) as executor:
    #Se crea el pool de threads.
    executor = ThreadPoolExecutor(max_workers=2) #Cuantos threads se van a crear.

    #Llamando a la función a ejecutar.
    executor.submit(function_to_excecute, 5, 20)
    executor.submit(function_to_excecute, 7, 15) #Se ejecutan al mismo tiempo los dos hilos que hicieron la solicitud. 

    executor.submit(function_to_excecute, 8, 48)
    executor.submit(function_to_excecute, 1, 1) #Se ejecutan al mismo tiempo los siguientes dos hilos que hicieron la solicitud-

    #Se pueden asignar tareas diferentes.
    executor.submit(greeting, 'Agustín')
    executor.submit(function_to_excecute, 8, 48) #Se ejecutan los dos últimos hilos al mismo tiempo.
    '''Aquí termina el ciclo de vida del pool'''