import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo6(threading.Thread):
    def __init__(self, name_hilo, nombre_archivo):
        super().__init__(name=name_hilo)
        self.name_hilo = name_hilo
        self.nombre_archivo = nombre_archivo

    def run(self):
        self.guardar_nombre()

    def guardar_nombre(self):
        nombres = []
        while True:
            nombre = input("Ingresa un nombre o escribe 'salir' para salir XD: ")
            if nombre.lower() == 'salir':
                break
            nombres.append(nombre)
            with open(self.nombre_archivo, 'a') as archivo:
                archivo.write(nombre + '\n')
            print("El nombre ha sido guardado correctamente.")
            print("Nombres guardados:")
            for nombre_guardado in nombres:
                print(nombre_guardado)

# Uso de la clase
nombre_archivo = "nombres.txt"
hilo6 = Hilo6("HiloDeNombres", nombre_archivo)



 
    


