import threading

def db_access():
    semaphore_access_db.acquire()
    #Código de base de datos.
    semaphore_access_db.release()

def db_access_with():
    with semaphore_access_db:
        pass


#Se crea el semáforo.
semaphore_access_db = threading.Semaphore(5)