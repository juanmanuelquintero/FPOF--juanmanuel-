import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo5(threading.Thread):
    def __init__(self,name_hilo,):
        threading.Thread.__init__(self, name=name_hilo, target=Hilo5.run)
        self.name_hilo=name_hilo
       

    def run(self):
        self.infinito()

    def infinito(self):
        while True:
            logging.debug('infinito')
            time.sleep(1)
        
    
    
