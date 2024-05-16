import re
import requests

response = requests.get("http://localhost:8000")

class Modelo_ropa:
    def __init__(self):
        self.marca = ""
        self.material = ""
        self.talla = ""
        self.color = ""

    def set_marca(self, marca):
        self.marca = marca

    def set_material(self, material):
        self.material = material

    def set_talla(self, talla):
        self.talla = talla

    def set_color(self, color):
        self.color = color

    def validar_datos(self):
        if not re.match("^[a-zA-Z0-9 ]+$", self.marca):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.material):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.talla):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.color):
            return False
        return True

    def enviarDatos(self):
        data = {
            "marca": self.marca,  
            "material": self.material,  
            "talla": self.talla,  
            "color": self.color  
        }

        response = requests.post("http://127.0.0.1:8000/v1/ropa",data)
        print(response.status_code)
        print(response.content)
