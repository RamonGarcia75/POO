from tkinter import *

ventana = Tk()
ventana.title("RadioButton")
ventana.geometry("500x500") 

def mostrarEstado():
      resultado.config(text="Opccion Slecionada ")
       
opcion=StringVar()
radioboton1=Radiobutton(ventana,text="Opcion 1", variable=opcion,value="Opcion1")
radioboton1.pack()

opcion=StringVar()
radioboton2=Radiobutton(ventana,text="Opcion 2", variable=opcion,value="Opcion2")
radioboton2.pack()

opcion=StringVar()
radioboton3=Radiobutton(ventana,text="Opcion 3", variable=opcion,value="Opcion3")
radioboton3.pack()



Button=Button(ventana,text="confirmar", command=mostrarEstado)
Button.pack()

resultado = Label(ventana,text="")
resultado.pack()

ventana.mainloop() 


