from tkinter import *

ventana=Tk()
ventana.title("entry")
ventana.geometry("500x500")

lbl_nombre=Label(ventana,Text="ingrese su nombre").pack()

txt_nombre=Entry(ventana,width=30)

btn_saludar=Button(ventana,text="saludar",command="")