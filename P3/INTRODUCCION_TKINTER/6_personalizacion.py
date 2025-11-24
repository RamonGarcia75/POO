from tkinter import *

ventana=Tk()

ventana.title("personalizar iwdgets u objeptos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="biemvenudo")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=["helvetica,30,italic"]
    relief=SOLID,
    border=2
)
etiqueta.pack(pady=25)

boton1=Button(ventana,text="hazclik")
boton1.config(
    bg="blue",
    fg="whigt",
    width=15,
    height=4,
    font=["Aial,20,blod"]
    relief=GROOVE,
    border=2,
    activeforeground="yellow",
    activebackground="red",

)

ventana.mainloop()

