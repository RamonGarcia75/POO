from tkinter import *

ventana = Tk()
ventana.title("CheckButton")
ventana.geometry("500x500") 

def mostrarEstado():
    if opcion.get()==1:
      resultado.config(text="Notificaciones Activadas ")
    else:
       resultado.config(text="Notificaciones Desactivadas ")
       

opcion=IntVar()
Checkboton=Checkbutton(ventana,text="¿deseas recibir notificaciones?", variable=opcion,onvalue=1,offvalue=0)
Checkboton.pack()

Button=Button(ventana,text="confirmar", command=mostrarEstado)
Button.pack()

resultado = Label(ventana,text="")
resultado.pack()

ventana.mainloop() 
