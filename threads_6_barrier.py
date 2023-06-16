import threading
import random
from time import sleep

def fun_to_execute():
    sleep(random.random() * 10) #Espera entre 0 y 10 segundos.
    print(f'{threading.current_thread().name} comienza ejecución...')

    barrier.wait()

    sleep(random.random() * 10) #Espera entre 0 y 10 segundos.
    print(f'{threading.current_thread().name} termina ejecución...')


#Se crean los hilos.
thread1 = threading.Thread(target=fun_to_execute, name='Hilo 1')
thread2 = threading.Thread(target=fun_to_execute, name='Hilo 2')
thread3 = threading.Thread(target=fun_to_execute, name='Hilo 3')
thread4 = threading.Thread(target=fun_to_execute, name='Hilo 4')

#Se crea la barrera para 4 hilos.
barrier = threading.Barrier(4)

#Se ejecutan los hilos.
thread1.start()
thread2.start()
thread3.start()
thread4.start()