import tkinter as tk

ventana = tk.Tk()
ventana.title("App")
ventana.geometry("450x230")
ventana.resizable(False,False)

etiqueta = tk.Label(ventana, text = "ingresa nombre")
etiqueta.pack()

ingreso_nombre= tk.Entry(ventana)
ingreso_nombre.pack()
def saludar():
    nombre = ingreso_nombre.get()
    saludo.config(text=f'hola {nombre},saludos')

boton = tk.Button(ventana,text="saludar",command=saludar, bg="cyan")
boton.pack()

saludo = tk.Label(ventana)
saludo.pack()

ventana.mainloop()