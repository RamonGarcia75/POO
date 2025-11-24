from tkinter import *


def mostrarEstado(tipo):
    if tipo == "nuevo":
        resultado.config(text=f"nuevo archivo")
    elif tipo == "nuevo":
        resultado.config(text=f"nuevo archivo")
    elif tipo == "nuevo":
        resultado.config(text=f"nuevo archivo")
    elif tipo == "nuevo":
        resultado.config(text=f"nuevo archivo")

    

ventana = Tk()
ventana.title("menu")
ventana.geometry("500x500") 

MenuBar=Menu(ventana)
ventana.config(menu=MenuBar)



archivomenu=Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="archivo", menu=archivomenu)
archivomenu.add_command(label="nuevo archivo",command=lambda:mostrarEstado("Nuevo Archivo"))
archivomenu.add_command(label="guardar archivo", command=lambda:mostrarEstado("Guardar Archivo"))
archivomenu.add_separator()
archivomenu.add_command(label="salir",command=ventana.quit)

edcicionmenu=Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="archivo", menu=edcicionmenu)
edcicionmenu.add_command(label="copiar",command=lambda:mostrarEstado("Copea Archivo"))
edcicionmenu.add_command(label="Recortar", command=lambda:mostrarEstado("recortar Archivo"))
edcicionmenu.add_separator()
edcicionmenu.add_command(label="salir",command=ventana.quit)

resultado = Label(ventana, text="")
resultado.pack()


ventana.mainloop() 
