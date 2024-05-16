import tkinter as tk
from tkinter import messagebox
from controllers.controlador import Controlador_ropa

class Vista_ropa:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("300x600")
        self.ventana.title("formulario")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="pink")
        self.ventana.config(cursor="heart")        
        self.controlador = Controlador_ropa()
        
        # Configuración de las entradas y etiquetas
        self.setup_entrada("marca", self.validar_caracteres_marca)
        self.setup_entrada("material", self.validar_caracteres_material)
        self.setup_entrada("talla", self.validar_caracteres_talla)
        self.setup_entrada("color", self.validar_caracteres_color)

        # Botón de validación
        self.button_validar = tk.Button(self.ventana, text="Guardar", command=self.validar_datos)
        self.button_validar.pack()

    def setup_entrada(self, campo, validation_method):
        label = tk.Label(self.ventana, text=f"{campo.capitalize()}:")
        label.pack()
        entry = tk.Entry(self.ventana)
        entry.pack()
        label_error = tk.Label(self.ventana, text="", fg="red",bg="pink")
        label_error.pack()
        entry.bind("<KeyRelease>", validation_method)
        setattr(self, f"entry_{campo}", entry)
        setattr(self, f"label_error_{campo}", label_error)

    def validar_datos(self):
        marca = self.entry_marca.get()
        material = self.entry_material.get()
        talla = self.entry_talla.get()
        color = self.entry_color.get()

        resultado = self.controlador.validar_datos(marca, material, talla, color)
        if resultado:
            messagebox.showinfo("Validación", "La información es válida.")
            resultado1 = self.controlador.enviar_datos(marca,material,talla,color)
            resultado1
        else:
            messagebox.showerror("Validación", "La información no es válida.")

    def validar_caracteres_marca(self, event):
        self.validar_caracteres_generico(self.entry_marca, self.label_error_marca)

    def validar_caracteres_material(self, event):
        self.validar_caracteres_generico(self.entry_material, self.label_error_material)

    def validar_caracteres_talla(self, event):
        self.validar_caracteres_generico(self.entry_talla, self.label_error_talla)

    def validar_caracteres_color(self, event):
        self.validar_caracteres_generico(self.entry_color, self.label_error_color)

    def validar_caracteres_generico(self, widget, label_error):
        texto = widget.get()
        if not self.controlador.validar_caracteres(texto):
            label_error.config(text="Solo caracteres válidos")
        else:
            label_error.config(text="")
