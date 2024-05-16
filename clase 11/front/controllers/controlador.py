from models.models import Modelo_ropa
import re

class Controlador_ropa:
    def __init__(self):
        self.modelo = Modelo_ropa()

    def validar_datos(self, marca, material, talla, color):
        self.modelo.set_marca(marca)
        self.modelo.set_material(material)
        self.modelo.set_talla(talla)
        self.modelo.set_color(color)

        return self.modelo.validar_datos()
    

    
    def validar_caracteres(self, texto):
        
        patron = re.compile(r'^[a-zA-Z0-9 ]+$')
        return bool(patron.match(texto))
    


    def enviar_datos(self, marca, material, talla, color):
        self.modelo.set_marca(marca)
        self.modelo.set_material(material)
        self.modelo.set_talla(talla)
        self.modelo.set_color(color)

        return self.modelo.enviarDatos()
    

