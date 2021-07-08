from threading import Thread, Semaphore
from time import sleep
import time
import logging
inicio = time.time()
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
    sleep(5)
def pensarDatos():
    logging.info("(Espera)Pensar que escribir")
    sleep(3)

def lector():
    global cl
    estado = True
    while(estado):
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
        estado = False

def escritor():
    estado = True
    while(estado):
      pensarDatos()
      bd.acquire()
      escribirBaseDatos()
      bd.release()
      estado = False


listaLectores = []    # Crear Lectores
for i in range(0, 10):
    l = Thread(target=lector)
    l.start()
    listaLectores.append(l)

listaEscritores = []    # Crear Escritores
for i in range(0, 10):
    esc = Thread(target=escritor)
    esc.start()
    listaEscritores.append(esc)

 # Esperar Lectores
for l in listaLectores:
    l.join()

# Esperar escritores
for e in listaEscritores:
    e.join()

fin = time.time()
print(fin - inicio)