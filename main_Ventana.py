from tkinter import *
from main_PPT import PPT
from tkinter import messagebox as mb
from random import randint

# ------------ Ventana Principal ------------
ventana = Tk()

# ------------ Declaracion de variables ------------
entrada_usuario = StringVar()
usuario = StringVar()
resultado_aux = StringVar()
computadora_aux = StringVar()

# ------------ Declaracion de funciones ------------
def ComenzarJuego():
    usuario = str(entrada_usuario.get().upper())
    if usuario != "PIEDRA" and usuario != "PAPEL" and usuario != "TIJERA":
        mb.showwarning("Error", "Ingrese un valor correcto entre 'Piedra', 'Papel' o 'Tijera'")
    else:
        eleccion = ["PIEDRA", "PAPEL", "TIJERA"]
        computadora = eleccion[randint(0, 2)]
        computadora_aux.set(computadora)
        resultado = PPT(usuario, computadora)
        resultado_aux.set(resultado)

def AppInfo():
    mb._show("Juego 1.0","Juega piedra, papel o tijera contra la computadora")


# ------------ Aspectos de ventana ------------
ventana.geometry("500x250")
ventana.resizable(0,0)
ventana.title("Piedra, Papel o Tijera")

# ------------ Barra de Menu ------------
mi_menu = Menu(ventana)

ventana.config(menu = mi_menu)
mi_menu.add_command(label = "About", command = AppInfo)
mi_menu.add_command(label = "Salir", command = ventana.quit)

# # ------------ Interfaz de ventana ------------
titulo = Label(ventana, text = "Bienvenido a PIEDRA, PAPEL o TIJERA")
titulo.config(
    fg="white",
    bg="blue",
    padx=100,
    pady=10,
    font=("Calibri", 18)
)
titulo.grid(row=0, columnspan=2, sticky=W)

texto_1 = Label(ventana, text="Ingrese su eleccion: ")
texto_1.config(
    fg = "blue",
    padx=10,
    pady=10,
    font=("Calibri", 12)
)
texto_1.grid(row=1, column=0, sticky=W)

entrada_user = Entry(ventana, textvariable=entrada_usuario)
entrada_user.grid(row=1, column=1, sticky=W,padx=15,pady=10)

boton = Button(ventana, text="Jugar", bg="blue", fg="white", command=ComenzarJuego)
boton.grid(row=2,column=0, sticky=E, padx=20, pady=12)

texto_2 = Label(ventana, text = "La computadora eligio: ")
texto_2.config(
    fg = "blue",
    padx=10,
    pady=10,
    font=("Calibri", 12)
)
texto_2.grid(row=3,column=0, sticky=W)

texto_3 = Label(ventana, textvariable=computadora_aux)
texto_3.config(
    fg = "blue",
    padx=10,
    pady=10,
    font=("Calibri", 12)
)
texto_3.grid(row =3, column=1, sticky=W)

texto_4 = Label(ventana, text="El ganador es: ")
texto_4.config(
    fg = "blue",
    padx=10,
    pady=10,
    font=("Calibri", 12)
)
texto_4.grid(row=4,column=0, sticky=W)

texto_5 = Label(ventana, textvariable=resultado_aux)
texto_5.config(
    fg = "red",
    padx=10,
    pady=10,
    font=("Calibri", 14)
)
texto_5.grid(row =4, column=1, sticky=W)

ventana.mainloop()