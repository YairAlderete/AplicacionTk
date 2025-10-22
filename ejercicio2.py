import tkinter as tk

ventana = tk.Tk()
ventana.title("bs")
ventana.geometry("450x230")
ventana.resizable(False,False)

frame1 = tk.Frame(ventana, bg="cyan",width="300", height="350", bd=4, relief="sunken")
frame1.pack()

gmail = tk.Label(frame1, text = "ingresa gmail", bg="cyan")
gmail.pack()
entrada_gmail= tk.Entry(frame1)
entrada_gmail.pack()

contrasena = tk.Label(frame1, text="ingresa la contraseña", bg="cyan")
contrasena.pack(pady=10)
ingreso_contrasena= tk.Entry(frame1)
ingreso_contrasena.pack()



gmail_correcto= "pepe573"
contrasena_correcta= "123456"

def sesion():
    gmail = entrada_gmail.get()
    contrasena = ingreso_contrasena.get()
    
    if gmail==gmail_correcto and contrasena == contrasena_correcta:
        mensajeB.config(text=f'inicio de sesioj cojn exito')
    else:
        mensajeB.config(text=f'gmail o contraseña incorrecta')

botonIinicar= tk.Button(frame1, text="iniciar sesion", command=sesion,bg="green")
botonIinicar.pack()

mensajeB =tk.Label(frame1)
mensajeB.pack()


ventana.mainloop()







