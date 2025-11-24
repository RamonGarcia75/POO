from tkinter import *
from tkinter import ttk

def progreso ():
    barraprogreso["value"]=0
    ventana.update()
    for i in range(101):
        barraprogreso["value"]=i
        ventana.update()
        ventana.after(50)

ventana = Tk()
ventana.title("progresbar")
ventana.geometry("500x500") 

barraprogreso=ttk.Progressbar(ventana,mode="determinate",length=200)
barraprogreso.pack()

boton=Button(ventana, text="iniciar proceso", command=progreso)
boton.pack()

ventana.mainloop() 
