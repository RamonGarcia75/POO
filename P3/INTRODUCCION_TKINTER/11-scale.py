from tkinter import *

ventana = Tk()
ventana.title("scale")
ventana.geometry("500x500") 

def mostrarEstado():
      resultado.config(text="selecions por el usuario: {valor.get()} ")
       

valor=IntVar()
escala=Scale(ventana,from_=0,to=100,orient=HORIZONTAL,variable=valor)
escala.pack

boton= Button(ventana,text="confirmar", command=mostrarEstado)
boton.pack()


resultado = Label(ventana,text="")
resultado.pack()

ventana.mainloop() 

