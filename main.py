from threading import Thread, Lock, Semaphore
from time import sleep
from random import randint
import logging

mutex = Lock()
bd = Semaphore(1)
lectores = 0

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')


def leerBaseDatos():
    sleep(randint(3, 6))


def escribirBaseDatos(nEscritor):
    sleep(randint(5, 10))


#######
def lector():
    global lectores

    while (True):
        logging.info("Lectura")
        ####Para Incrementar los Lectores y apoderarse de la base de datos...
        mutex.acquire()
        lectores += 1

        if lectores == 1:
            bd.acquire()

        mutex.release()

        ####
        leerBaseDatos()
        ####

        ##### Decrementar los Lectores y librerar la base de datos
        mutex.acquire()
        lectores -= 1

        if lectores == 0:
            bd.release()
            sleep(randint(2, 5))

        mutex.release()
        sleep(randint(2, 5))


def escritor(nEscritor):
    while (True):
        logging.info("Escribir")
        bd.acquire()
        escribirBaseDatos(nEscritor)
        bd.release()

        sleep(randint(2, 5))


escritor1 = Thread(target=escritor, args=(1,))
escritor2 = Thread(target=escritor, args=(2,))
escritor3 = Thread(target=escritor, args=(3,))

lector1 = Thread(target=lector)
lector2 = Thread(target=lector)
lector3 = Thread(target=lector)

lector1.start()
lector2.start()
lector3.start()

escritor1.start()
escritor2.start()
escritor3.start()

escritor1.join()
