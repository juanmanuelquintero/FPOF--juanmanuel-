import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo4(threading.Thread):
    def __init__(self,name_hilo,name_persona):
        threading.Thread.__init__(self, name=name_hilo, target=Hilo4.run)
        self.name_hilo=name_hilo
        self.name_persona=name_persona

    def run(self):
        self.consultar(self.name_persona)

    def consultar(self,name_persona):
        logging.debug('consultando: '+ name_persona)
        time.sleep(5)
        return
        
    
    
