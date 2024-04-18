import tkinter as tk
from datetime import datetime
import re
from tkinter import messagebox


import requests

response = requests.get("http://127.0.0.1:8000/")
#print(response.content)


ventana = tk.Tk()
ventana.geometry("600x600")
ventana.resizable(0, 0)
ventana.config(cursor="heart")
ventana.config(relief="groove") 
ventana.config(bd=4) 
ventana.title("Formulario")
ventana.configure(bg="#FAEBD7")

def validar_material(evento):
    texto_ingresado = material.get()
    if re.match("^[A-Za-z ]+$", texto_ingresado):
        material_error.config(text="")
    else:
        material_error.config(text="¡No se permiten caracteres especiales ni numeros!")

def validar_color(evento):
    texto_ingresado = color.get()
    if re.match("^[A-Za-z ]+$", texto_ingresado):
        color_error.config(text="")
    else:
        color_error.config(text="¡No permiten caracteres especiales ni numeros!")

def validar_talla(evento):
    texto_ingresado = talla.get()
    if re.match("^[0-9a-zA-Z ]+$", texto_ingresado):
        talla_error.config(text="")
    else:
        talla_error.config(text="¡No se permiten caracteres especiales!")

def validar_marca(evento):
    texto_ingresado = marca.get()
    if re.match("^[0-9a-zA-Z ]+$", texto_ingresado):
        marca_error.config(text="")
    else:
        marca_error.config(text="¡No se permiten ni caracteres especiales!")


def validar_informacion():
    material_ = re.match("^[A-Za-z ]+$", material.get())
    color_ = re.match("^[A-Za-z ]+$", color.get())
    marca_ = re.match("^[0-9a-zA-Z ]+$", marca.get())
    talla_ = re.match("^[0-9a-zA-Z ]+$", talla.get())

    if material_ and color_ and marca_ and talla_:
        messagebox.showinfo("Validación Exitosa", "Todos los campos han sido completados correctamente.")

        data = {
            "material": material.get(),
            "color": color.get() ,
            "talla":  talla.get(),
            "marca": marca.get()
        }
        response=requests.post("http://127.0.0.1:8000/v1/ropa", data)
        print(response.status_code)
        print(response.content)

    else:
        messagebox.showwarning("Advertencia", "Por favor completa todos los campos correctamente.")

material = tk.StringVar()
color = tk.StringVar()
marca = tk.StringVar()
talla = tk.StringVar()


# Configuración del título
titulo = tk.Label(ventana, text="Formulario", font=("Arial", 14), bg="#FAEBD7")
titulo.grid(columnspan=2, pady=10)

# Configuración de las cajas de texto y las etiquetas de error
label1 = tk.Label(ventana, text="material:", bg="#FAEBD7").grid(column=0, row=1, padx=30, pady=20)
t1 = tk.Entry(ventana, width=24, textvariable=material)
t1.grid(column=1, row=1, padx=30, pady=5)
material_error = tk.Label(ventana, text="", fg="red", bg="#FAEBD7")
material_error.place(x=160, y=90)

label2 = tk.Label(ventana, text="color:", bg="#FAEBD7").grid(column=0, row=2, padx=30, pady=20)
t2 = tk.Entry(ventana, width=24, textvariable=color)
t2.grid(column=1, row=2, padx=30, pady=5)
color_error = tk.Label(ventana, text="", fg="red", bg="#FAEBD7")
color_error.place(x=160, y=150)

label3 = tk.Label(ventana, text="marca:", bg="#FAEBD7").grid(column=0, row=3, padx=30, pady=20)
t3 = tk.Entry(ventana, width=24, textvariable=marca)
t3.grid(column=1, row=3, padx=30, pady=5)
talla_error = tk.Label(ventana, text="", fg="red", bg="#FAEBD7")
talla_error.place(x=180, y=270)

label4 = tk.Label(ventana, text="talla:", bg="#FAEBD7").grid(column=0, row=4, padx=30, pady=20)
t4 = tk.Entry(ventana, width=24, textvariable=talla)
t4.grid(column=1, row=4, padx=30, pady=5)
marca_error = tk.Label(ventana, text="", fg="red", bg="#FAEBD7")
marca_error.place(x=170, y=210)



boton_validar = tk.Button(ventana, text="Agregar", height=4, width=30, bg="#F0F8FF", command=validar_informacion)
boton_validar.grid(row=7, column=1, pady=10)


# Enlace de las cajas de texto con los eventos del teclado
t1.bind("<KeyRelease>", validar_material)
t2.bind("<KeyRelease>", validar_color)
t3.bind("<KeyRelease>", validar_marca)
t4.bind("<KeyRelease>", validar_talla)

ventana.mainloop()
