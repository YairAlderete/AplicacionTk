import tkinter as tk

ventana = tk.Tk()
ventana.title("bs")
ventana.geometry("450x230")
ventana.resizable(False,False)

gmail = tk.Label(ventana, text = "ingresa gmail")
gmail.pack()
ingreso_contraseña= tk.Entry(ventana)

ingreso_contraseña.pack()
contrasena = tk.Label(ventana, text="ingresa la contraseña")
contrasena.pack()

ingreso_contraseña= tk.Entry(ventana)
ingreso_contraseña.pack()

gmail_correcto= "pepe573"

ingreso_contraseña= "123456"

def sesion():
    usuario = gmail_correcto.get()
    contrasena = ingreso_contraseña.get()
    
    if gmail==gmail_correcto and contrasena ==ingreso_contraseña:
        mensajeB.config(text=f'inicio de sesioj cojn exito')
    else:
        mensajeB.config(text=f'gmail o contraseña incorrecta')

botonIinicar= tk.Button(ventana, text="iniciar sesion", command=sesion,bg="green")
botonIinicar.pack()

ventana.mainloop







mensajeB =tk.Label(ventana)
mensajeB.pack()