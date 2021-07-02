from threading import Thread, Semaphore
from time import sleep
import logging

mutex = Semaphore(1)
bd = Semaphore(1)
cl = 0

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def leerBaseDatos():
    logging.info("Leer Base de Datos")
    sleep(3)

def usarBasedeDatos():
    logging.info("Usar Lectura de Datos")
    sleep(4)

def escribirBaseDatos():
    logging.info("Escribir Base de Datos")
    sleep(10)

def pensarDatos():
    logging.info("(Espera)Pensar que escribir")
    sleep(6)


def lector():
    global cl
    while(True):
        mutex.acquire()
        cl = cl + 1
        if cl == 1:
            bd.acquire()
        mutex.release()
        leerBaseDatos()
        mutex.acquire()
        cl = cl - 1
        if cl==0:
            bd.release()
        mutex.release()
        usarBasedeDatos()

def escritor():
    while(True):
      pensarDatos()
      bd.acquire()
      escribirBaseDatos()
      bd.release()

escritor1 = Thread(target=escritor)
escritor2 = Thread(target=escritor)
escritor3 = Thread(target=escritor)

lector1 = Thread(target=lector)
lector2 = Thread(target=lector)
lector3 = Thread(target=lector)

lector1.start()
lector2.start()
lector3.start()

escritor1.start()
escritor2.start()
escritor3.start()
