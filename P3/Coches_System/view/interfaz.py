# Importación del controlador para acceder a la lógica de la aplicación
from controller.controlador import Controlador as funciones 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Coches System")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.menu_principal()
        self.lbl_bienvenida = Label(self.ventana, text="Bienvenido al Sistema\nSeleccione una opción del Menú", font=("Arial", 20))
        self.lbl_bienvenida.pack(expand=True)

    def borrarPantalla(self):
        """Limpia todos los widgets de la ventana actual."""
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_principal(self):
        """Define la barra de menú principal."""
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)
        menuArchivo = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Sistema", menu=menuArchivo)
        menuArchivo.add_command(label="Salir", command=self.ventana.quit)
        
        # Opciones del menú para cada tipo de vehículo (mejor que la pantalla intermedia)
        menuAutos = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Autos", menu=menuAutos)
        menuAutos.add_command(label="Insertar Auto", command=self.insertar_autos)
        menuAutos.add_command(label="Consultar Autos", command=self.consultar_autos)
        menuAutos.add_command(label="Cambiar Auto", command=self.cambiar_autos)
        menuAutos.add_command(label="Borrar Auto", command=self.borrar_autos)
        
        menuCamiones = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Camiones", menu=menuCamiones)
        menuCamiones.add_command(label="Insertar Camión", command=self.insertar_camiones)
        menuCamiones.add_command(label="Consultar Camiones", command=self.consultar_camiones)
        menuCamiones.add_command(label="Cambiar Camión", command=self.cambiar_camiones)
        menuCamiones.add_command(label="Borrar Camión", command=self.borrar_camiones)
        
        menuCamionetas = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Camionetas", menu=menuCamionetas)
        menuCamionetas.add_command(label="Insertar Camioneta", command=self.insertar_camionetas)
        menuCamionetas.add_command(label="Consultar Camionetas", command=self.consultar_camionetas)
        menuCamionetas.add_command(label="Cambiar Camioneta", command=self.cambiar_camionetas)
        menuCamionetas.add_command(label="Borrar Camioneta", command=self.borrar_camionetas)

    def menu_acciones(self, tipo):
        """Redirige al menú principal (ya no es una pantalla de botones intermedios)."""
        self.borrarPantalla()
        self.menu_principal()
        self.lbl_bienvenida = Label(self.ventana, text=f"Acciones de {tipo} completadas.\nSeleccione otra opción del Menú.", font=("Arial", 20))
        self.lbl_bienvenida.pack(expand=True)


    # --- UTILIDAD ---
    def _crear_entry(self, parent, text, variable):
        """Función auxiliar para crear etiquetas y entradas de forma consistente."""
        frame = Frame(parent)
        frame.pack(pady=2, fill="x")
        Label(frame, text=text, width=20, anchor="e").pack(side="left")
        Entry(frame, textvariable=variable).pack(side="left", expand=True, fill="x")

    def _mostrar_datos_en_treeview(self, ventana, datos, columnas, titulo, tipo_vehiculo):
        """Función auxiliar para mostrar resultados de consulta en una tabla Treeview."""
        self.borrarPantalla()
        Label(ventana, text=titulo, font=("Arial", 16)).pack(pady=10)
        
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        # Configurar encabezados y ancho de columnas
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=80, anchor="center")
            
        # Insertar los datos
        if datos:
            for fila in datos:
                tree.insert("", "end", values=fila)
        else:
            Label(ventana, text="No se encontraron registros.", fg="red").pack(pady=10)

        tree.pack(fill="both", expand=True, padx=20, pady=10)
        Button(ventana, text="Volver", command=lambda: self.menu_acciones(tipo_vehiculo)).pack(pady=10)


    # ----------------------------------------
    # AUTOS
    # ----------------------------------------

    def insertar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR AUTO", font=("Arial", 16)).pack(pady=10)
        
        v_marca = StringVar()
        v_color = StringVar()
        v_modelo = StringVar()
        v_velocidad = IntVar()
        v_caballaje = IntVar()
        v_plazas = IntVar()
        
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "Marca:", v_marca)
        self._crear_entry(frm, "Color:", v_color)
        self._crear_entry(frm, "Modelo:", v_modelo)
        self._crear_entry(frm, "Velocidad:", v_velocidad)
        self._crear_entry(frm, "Caballaje:", v_caballaje)
        self._crear_entry(frm, "Plazas:", v_plazas)
        
        Button(self.ventana, text="Guardar Auto", bg="#4CAF50", fg="white",
               # Llama al controlador
               command=lambda: funciones.insertar_auto(
                   v_marca.get(), v_color.get(), v_modelo.get(), v_velocidad.get(), v_caballaje.get(), v_plazas.get()
               )).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def consultar_autos(self):
        # 1. Obtener datos del controlador
        datos_autos = funciones.consultar_autos() 
        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas")
        
        # 2. Mostrar
        self._mostrar_datos_en_treeview(self.ventana, datos_autos, cols, "CONSULTA DE AUTOS", "Autos")

    def cambiar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR (ACTUALIZAR) AUTO", font=("Arial", 16)).pack(pady=10)
        
        v_id = IntVar()
        v_marca = StringVar() # Se usa solo para la nueva marca
        
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID del Auto a cambiar:", v_id)
        self._crear_entry(frm, "Nueva Marca (Ejemplo):", v_marca)
        
        Button(self.ventana, text="Actualizar", bg="#FFC107", 
               # Llama al controlador
               command=lambda: funciones.cambiar_auto(v_id.get(), v_marca.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def borrar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR AUTO", font=("Arial", 16)).pack(pady=10)
        
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID del Auto a borrar:", v_id)
        
        Button(self.ventana, text="Eliminar Definitivamente", bg="#F44336", fg="white",
               # Llama al controlador
               command=lambda: funciones.borrar_auto(v_id.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()


    # ----------------------------------------
    # CAMIONETAS
    # ----------------------------------------

    def insertar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR CAMIONETA", font=("Arial", 16)).pack(pady=10)
        
        # Variables de entrada
        v_marca, v_color, v_modelo = StringVar(), StringVar(), StringVar()
        v_vel, v_cab, v_pla = IntVar(), IntVar(), IntVar()
        v_trac = StringVar()
        v_cerrada = BooleanVar() # Para el Checkbutton
        
        frm = Frame(self.ventana)
        frm.pack()
        
        # Campos comunes
        self._crear_entry(frm, "Marca:", v_marca)
        self._crear_entry(frm, "Color:", v_color)
        self._crear_entry(frm, "Modelo:", v_modelo)
        self._crear_entry(frm, "Velocidad:", v_vel)
        self._crear_entry(frm, "Caballaje:", v_cab)
        self._crear_entry(frm, "Plazas:", v_pla)
        
        # Campos específicos de camionetas
        self._crear_entry(frm, "Tracción (4x4, 4x2...):", v_trac)
        Checkbutton(frm, text="¿Es Cerrada?", variable=v_cerrada).pack(pady=5, anchor="w")
        
        Button(self.ventana, text="Guardar Camioneta", bg="#4CAF50", fg="white",
               # Llama al controlador
               command=lambda: funciones.insertar_camioneta(
                   v_marca.get(), v_color.get(), v_modelo.get(), v_vel.get(), v_cab.get(), 
                   v_pla.get(), v_trac.get(), v_cerrada.get()
               )).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def consultar_camionetas(self):
        # 1. Obtener datos del controlador
        datos_camionetas = funciones.consultar_camionetas()
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Tracción", "Cerrada")
        
        # 2. Mostrar
        self._mostrar_datos_en_treeview(self.ventana, datos_camionetas, cols, "CONSULTA CAMIONETAS", "Camionetas")

    def cambiar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR CAMIONETA", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID de Camioneta a cambiar:", v_id)
        
        Button(self.ventana, text="Actualizar (Ejemplo)", bg="#FFC107", 
               # Llama al controlador
               command=lambda: funciones.cambiar_camioneta(v_id.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def borrar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR CAMIONETA", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID de Camioneta a borrar:", v_id)
        
        Button(self.ventana, text="Borrar Definitivamente", bg="#F44336", fg="white", 
               # Llama al controlador
               command=lambda: funciones.borrar_camioneta(v_id.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()


    # ----------------------------------------
    # CAMIONES
    # ----------------------------------------
    
    def insertar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR CAMIÓN", font=("Arial", 16)).pack(pady=10)
        
        # Variables de entrada (8 en total)
        v_marca, v_color, v_modelo = StringVar(), StringVar(), StringVar()
        v_vel, v_cab, v_pla, v_ejes, v_cap_carga = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
        
        v_vars = [v_marca, v_color, v_modelo, v_vel, v_cab, v_pla, v_ejes, v_cap_carga]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Cap. Carga (Kg)"]
        
        frm = Frame(self.ventana)
        frm.pack()
        
        for i, txt in enumerate(labels):
            self._crear_entry(frm, txt + ":", v_vars[i])
            
        Button(self.ventana, text="Guardar Camión", bg="#4CAF50", fg="white",
               # Llama al controlador
               command=lambda: funciones.insertar_camion(*[v.get() for v in v_vars])).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def consultar_camiones(self):
        # 1. Obtener datos del controlador
        datos_camiones = funciones.consultar_camiones()
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Ejes", "Carga")
        
        # 2. Mostrar
        self._mostrar_datos_en_treeview(self.ventana, datos_camiones, cols, "CONSULTA CAMIONES", "Camiones")

    def cambiar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR CAMIÓN", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID de Camión a cambiar:", v_id)
        
        Button(self.ventana, text="Actualizar (Ejemplo)", bg="#FFC107", 
               # Llama al controlador
               command=lambda: funciones.cambiar_camion(v_id.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def borrar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR CAMIÓN", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID de Camión a borrar:", v_id)
        
        Button(self.ventana, text="Borrar Definitivamente", bg="#F44336", fg="white", 
               # Llama al controlador
               command=lambda: funciones.borrar_camion(v_id.get())).pack(pady=20)
        
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()