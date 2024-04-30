import threading
import datetime
import logging
import time
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG)

tiempo_inicial=datetime.datetime.now()

def consultar(nombre):
    logging.debug('consultando:'+ nombre)
    time.sleep(5)
    return

def letras():
    list=['a','b','c','d','e']
    for elemento in list:
        logging.debug(elemento)
        time.sleep(1)
    return

def numeros():
    list=[1,2,3,4,5]
    for elemento in list:
        logging.debug(elemento)
        time.sleep(2)
    return
def main():
    nombre_archivo = "nombres.txt"
    mi_hilo = Hilo6("HiloDeNombres", nombre_archivo)
    mi_hilo.start() 

hilo1=threading.Thread(name='hilo1',target=numeros)
hilo2=threading.Thread(name='hilo2',target=letras)
hilo3=threading.Thread(name='hilo3',target=consultar,args=('juan',))
hilo4=Hilo4('hilo4','juan')
hilo5=Hilo5('hilo5')
hilo6=threading.Thread(name='hilo6',target=main)


#hilo1.start()S
#hilo1.join()

#hilo2.start()
#hilo2.join()

#hilo3.start()
#hilo3.join()
#hilo4.start()
hilo5.start()
hilo6.start()






tiempo_finalizado=datetime.datetime.now()

logging.debug('tiempotranscurrido:'+ str(tiempo_finalizado.second -tiempo_inicial.second) + '\n')

