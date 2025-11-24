from tkinter import *

ventana = Tk()
ventana.title("ListBox")
ventana.geometry("500x500") 

def mostratestado():
    selecion=lista.get(lista.curselection())
    resultado.config(text=f"selecioaste: {selecion}")

lista=Listbox(ventana,width=10,height=5,selectmode="SINGLE")
lista.pack()

opciones=["Amarilo","Rojo","azul","morado"]
for i in opciones:
    lista.insert(END,i)


boton = Button(ventana, text="mostrar selecion del usuario", command=mostratestado)
boton.pack

resultado= Label(ventana,text="")
resultado.pack()

ventana.mainloop() 
