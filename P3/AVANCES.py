"""""
3 Diciembre
1)Interfaces:
1.1 insertar_camionetas()
1.2 consultar_camionetas()
1.3 cambiar_camionetas()
1.4 borrar_camionetas()
2.1 insertar_camionetas()
2.2 consultar_camionetas()
2.3 cambiar_camionetas()
2.4 borrar_camionetas()

productos entregables:
interacion con todas las interfaces nobre del commint: "commit_03_12_25"

"""
from tkinter import *
from tkinter import messagebox
from controller import controlador

# --- VISTA DEL SISTEMA ---
class VistaSistema():
    def _init_(self, ventana):
        ventana.title("Administración Vehicular")
        ventana.geometry("600x600")
        VistaSistema.inicio_menu(ventana)

    # Utilería para limpiar la ventana
    def limpiar_frame(ventana):
        elementos = ventana.winfo_children()
        for elem in elementos:
            elem.destroy()

    # PANTALLA DE INICIO
    def inicio_menu(ventana):
        VistaSistema.limpiar_frame(ventana)
        
        titulo_principal = Label(ventana, text="Control de Flotilla", font=("Arial", 14))
        titulo_principal.pack(pady=10)
        
        # Botones principales
        btn_coches = Button(ventana, text="Automóviles", width=20, 
                            command=lambda: VistaSistema.panel_operaciones(ventana, "Autos"))
        btn_coches.pack(pady=(20, 5))
        
        btn_vans = Button(ventana, text="Camionetas", width=20, 
                          command=lambda: VistaSistema.panel_operaciones(ventana, "Camionetas"))
        btn_vans.pack(pady=5)
        
        btn_pesados = Button(ventana, text="Camiones", width=20, 
                             command=lambda: VistaSistema.panel_operaciones(ventana, "Camiones"))
        btn_pesados.pack(pady=5)
        
        boton_cerrar = Button(ventana, text="Cerrar Sistema", command=ventana.quit, bg="red", fg="white")
        boton_cerrar.pack(pady=40)

    # MENU DE OPERACIONES (antes menu_acciones)
    def panel_operaciones(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        
        etiqueta_cat = Label(ventana, text=f"Operaciones: {categoria}", font=("Arial", 12, "bold"))
        etiqueta_cat.pack(pady=10)
        
        # Mapeo de botones
        btn_add = Button(ventana, text="Registrar Nuevo", width=15,
                         command=lambda: VistaSistema.registrar_coche(ventana, categoria))
        btn_add.pack(pady=(15, 5))
        
        btn_view = Button(ventana, text="Ver Registros", width=15,
                          command=lambda: VistaSistema.listar_coche(ventana, categoria))
        btn_view.pack(pady=5)
        
        btn_edit = Button(ventana, text="Modificar", width=15,
                          command=lambda: VistaSistema.editar_coche(ventana, categoria))
        btn_edit.pack(pady=5)
        
        btn_del = Button(ventana, text="Dar de Baja", width=15,
                         command=lambda: VistaSistema.eliminar_coche(ventana, categoria))
        btn_del.pack(pady=5)
        
        btn_back = Button(ventana, text="Regresar al Menú", 
                          command=lambda: VistaSistema.inicio_menu(ventana))
        btn_back.pack(pady=30)

    # --- SECCIÓN AUTOMOVILES (Y GENERAL) ---

    def registrar_coche(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Registro de {categoria}").pack(pady=5)

        # Variables y Entradas
        v_marca = StringVar()
        Label(ventana, text="Fabricante/Marca:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_marca).pack()

        v_color = StringVar()
        Label(ventana, text="Color:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_color).pack()

        v_modelo = StringVar()
        Label(ventana, text="Modelo (Año):").pack(pady=(5,0))
        Entry(ventana, textvariable=v_modelo).pack()

        v_kph = IntVar()
        Label(ventana, text="Vel. Máxima:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_kph).pack()

        # Cambio de nombre solicitado: Caballaje -> Potencia
        v_potencia = IntVar()
        Label(ventana, text="Potencia (HP):").pack(pady=(5,0))
        Entry(ventana, textvariable=v_potencia).pack()

        # Cambio de nombre solicitado: Plazas -> Asientos
        v_asientos = IntVar()
        Label(ventana, text="Asientos:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_asientos).pack()

        # CAMPOS EXTRAS (Heredados de la lógica original)
        # Camionetas
        v_traccion = IntVar()
        Label(ventana, text="Tipo Tracción:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_traccion).pack()

        v_cerrada = StringVar()
        Label(ventana, text="¿Es Cerrada? (S/N):").pack(pady=(5,0))
        Entry(ventana, textvariable=v_cerrada).pack()

        # Camiones
        v_ejes = IntVar()
        Label(ventana, text="Num. Ejes:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_ejes).pack()

        v_capacidad = IntVar()
        Label(ventana, text="Capacidad Carga:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_capacidad).pack()

        Button(ventana, text="Guardar Datos").pack(pady=(20,0))
        Button(ventana, text="Cancelar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,20))

    def listar_coche(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Base de datos: {categoria}").pack(pady=5)
        Label(ventana, text=f"Sin resultados en {categoria} actualmente.").pack(pady=20)
        Button(ventana, text="Atrás", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=30)

    def editar_coche(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Edición en {categoria}").pack(pady=5)
        
        # ID para buscar
        v_id = IntVar()
        Label(ventana, text="ID Vehículo:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_id).pack()

        # Campos a editar
        v_marca = StringVar()
        Label(ventana, text="Nueva Marca:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_marca).pack()

        v_color = StringVar()
        Label(ventana, text="Nuevo Color:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_color).pack()

        v_modelo = StringVar()
        Label(ventana, text="Nuevo Modelo:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_modelo).pack()

        v_kph = IntVar()
        Label(ventana, text="Nueva Vel. Máx:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_kph).pack()

        v_potencia = IntVar()
        Label(ventana, text="Nueva Potencia:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_potencia).pack()

        v_asientos = IntVar()
        Label(ventana, text="Nuevos Asientos:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_asientos).pack()

        # Extras Camionetas/Camiones
        v_traccion = IntVar()
        Label(ventana, text="Nueva Tracción:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_traccion).pack()

        v_cerrada = StringVar()
        Label(ventana, text="Cerrada (S/N):").pack(pady=(5,0))
        Entry(ventana, textvariable=v_cerrada).pack()

        v_ejes = IntVar()
        Label(ventana, text="Ejes:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_ejes).pack()

        v_capacidad = IntVar()
        Label(ventana, text="Capacidad:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_capacidad).pack()

        Button(ventana, text="Actualizar").pack(pady=(20,0))
        Button(ventana, text="Cancelar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,20))

    def eliminar_coche(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Eliminar registro en {categoria}").pack(pady=5)
        
        v_id = IntVar()
        Label(ventana, text="Ingrese ID a borrar:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_id).pack()
        
        Button(ventana, text="Confirmar Baja").pack(pady=(20,0))
        Button(ventana, text="Atrás", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,20))

    # --- SECCIÓN CAMIONES (REORDENADA AL FINAL) ---
    
    # Nota: En tu código original, 'insertar_autos' contenía campos de camiones.
    # Aquí he separado las funciones específicas de camiones que tenías aparte para cumplir con el cambio de estructura.

    def registrar_camion_pesado(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Alta de {categoria} (Pesados)").pack(pady=5)
        
        v_idn = IntVar()
        Label(ventana, text="Identificador:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_idn).pack()
        
        v_marca = StringVar()
        Label(ventana, text="Fabricante:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_marca).pack()
        
        v_color = StringVar()
        Label(ventana, text="Color Chasis:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_color).pack()
        
        v_modelo = StringVar()
        Label(ventana, text="Año Modelo:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_modelo).pack()
        
        v_vel = IntVar()
        Label(ventana, text="Límite Velocidad:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_vel).pack()
        
        Button(ventana, text="Archivar").pack(pady=(30,0))
        Button(ventana, text="Regresar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,30))

    def listar_camion_pesado(ventana, categoria):
        # Misma logica de consulta pero separada al final
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Bitácora de {categoria}").pack(pady=5)
        Label(ventana, text=f"Base de datos vacía para {categoria}").pack(pady=10)
        Button(ventana, text="Regresar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=50)

    def editar_camion_pesado(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Modificar {categoria}").pack(pady=5)
        
        v_idn = IntVar()
        Label(ventana, text="ID Objetivo:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_idn).pack()
        
        # Campos reducidos según tu código original para camiones
        v_marca = StringVar()
        Label(ventana, text="Marca:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_marca).pack()
        
        v_color = StringVar()
        Label(ventana, text="Color:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_color).pack()
        
        v_modelo = StringVar()
        Label(ventana, text="Modelo:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_modelo).pack()
        
        v_vel = IntVar()
        Label(ventana, text="Velocidad:").pack(pady=(5,0))
        Entry(ventana, textvariable=v_vel).pack()
        
        Button(ventana, text="Sobreescribir").pack(pady=(30,0))
        Button(ventana, text="Regresar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,30))

    def eliminar_camion_pesado(ventana, categoria):
        VistaSistema.limpiar_frame(ventana)
        Label(ventana, text=f"Baja de {categoria}").pack(pady=5)
        
        v_idn = IntVar()
        Label(ventana, text="ID a eliminar:").pack(pady=(10,0))
        Entry(ventana, textvariable=v_idn).pack()
        
        Button(ventana, text="Eliminar Definitivamente").pack(pady=(30,0))
        Button(ventana, text="Regresar", command=lambda: VistaSistema.panel_operaciones(ventana, categoria)).pack(pady=(5,30))
