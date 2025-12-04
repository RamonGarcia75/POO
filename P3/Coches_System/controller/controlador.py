# Importamos las funciones del modelo
from model.modelo_coches import GestorVehicular 
from tkinter import messagebox

class Controlador:
    """
    Clase que maneja la lógica de la aplicación (Validación, Lógica de Negocio), 
    actuando como intermediario entre la Vista y el Modelo.
    """

    @staticmethod
    def _validar_campos_comunes(marca, color, modelo, velocidad, caballaje, plazas):
        """Validación genérica para campos comunes a todos los vehículos."""
        if not marca or not color or not modelo:
            messagebox.showwarning("Faltan Datos", "Los campos Marca, Color y Modelo son obligatorios.")
            return False
        try:
            # Validación de tipos y valores positivos
            if int(velocidad) <= 0 or int(caballaje) <= 0 or int(plazas) <= 0:
                 messagebox.showwarning("Datos Inválidos", "Velocidad, Caballaje y Plazas deben ser números positivos.")
                 return False
        except ValueError:
            messagebox.showwarning("Datos Inválidos", "Velocidad, Caballaje y Plazas deben ser números enteros válidos.")
            return False
        return True

    # ----------------------------------------
    # 1. AUTOS (Métodos del 4 DICIEMBRE)
    # ----------------------------------------
    
    @staticmethod
    def insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
        if not Controlador._validar_campos_comunes(marca, color, modelo, velocidad, caballaje, plazas):
            return
        
        if GestorVehicular.insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
            messagebox.showinfo("Éxito", "Automóvil registrado correctamente.")

    @staticmethod
    def consultar_autos():
        autos = GestorVehicular.consultar_autos()
        if not autos:
            messagebox.showinfo("Consulta", "No se encontraron registros de autos.")
        return autos
            
    @staticmethod
    def cambiar_auto(id_auto, nueva_marca):
        if not id_auto or not nueva_marca:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID y la nueva Marca.")
            return
        if GestorVehicular.cambiar_auto(id_auto, nueva_marca):
            messagebox.showinfo("Éxito", f"Auto con ID {id_auto} actualizado a marca {nueva_marca}.")
            
    @staticmethod
    def borrar_auto(id_auto):
        if not id_auto:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID del Auto a borrar.")
            return
        if GestorVehicular.borrar_auto(id_auto):
            messagebox.showinfo("Éxito", f"Auto con ID {id_auto} eliminado correctamente.")


    # ----------------------------------------
    # 2. CAMIONETAS (Métodos del 3 DICIEMBRE: 1.1 a 1.4)
    # ----------------------------------------

    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if not Controlador._validar_campos_comunes(marca, color, modelo, velocidad, caballaje, plazas):
            return
        if not traccion:
            messagebox.showwarning("Faltan Datos", "El campo Tracción es obligatorio para Camionetas.")
            return
            
        if GestorVehicular.insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
            messagebox.showinfo("Éxito", "Camioneta registrada correctamente.")

    @staticmethod
    def consultar_camionetas():
        camionetas = GestorVehicular.consultar_camionetas()
        if not camionetas:
             messagebox.showinfo("Consulta", "No se encontraron registros de camionetas.")
        return camionetas

    @staticmethod
    def cambiar_camioneta(id_camioneta):
        # Lógica de ejemplo (debes implementar el cambio de todos los campos en el modelo)
        if not id_camioneta:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID de la Camioneta a cambiar.")
            return
        if GestorVehicular.cambiar_camioneta(id_camioneta): 
            messagebox.showinfo("Éxito", f"Camioneta ID {id_camioneta} actualizada (Lógica a completar).")

    @staticmethod
    def borrar_camioneta(id_camioneta):
        if not id_camioneta:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID de la Camioneta a borrar.")
            return
        if GestorVehicular.borrar_camioneta(id_camioneta):
            messagebox.showinfo("Éxito", f"Camioneta con ID {id_camioneta} eliminada correctamente.")


    # ----------------------------------------
    # 3. CAMIONES (Métodos del 3 DICIEMBRE: 2.1 a 2.4)
    # ----------------------------------------

    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga):
        if not Controlador._validar_campos_comunes(marca, color, modelo, velocidad, caballaje, plazas):
            return
        if not ejes or not cap_carga:
            messagebox.showwarning("Faltan Datos", "Ejes y Cap. Carga son obligatorios para Camiones.")
            return
        try:
            # Validaciones específicas de camiones
            if int(ejes) <= 0 or int(cap_carga) <= 0:
                 messagebox.showwarning("Datos Inválidos", "Ejes y Capacidad de Carga deben ser números positivos.")
                 return
        except ValueError:
            messagebox.showwarning("Datos Inválidos", "Ejes y Capacidad de Carga deben ser números enteros.")
            return

        if GestorVehicular.insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga):
            messagebox.showinfo("Éxito", "Camión registrado correctamente.")

    @staticmethod
    def consultar_camiones():
        camiones = GestorVehicular.consultar_camiones()
        if not camiones:
             messagebox.showinfo("Consulta", "No se encontraron registros de camiones.")
        return camiones

    @staticmethod
    def cambiar_camion(id_camion):
        # Lógica de ejemplo (debes implementar el cambio de todos los campos en el modelo)
        if not id_camion:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID del Camión a cambiar.")
            return
        if GestorVehicular.cambiar_camion(id_camion): 
            messagebox.showinfo("Éxito", f"Camión ID {id_camion} actualizado (Lógica a completar).")

    @staticmethod
    def borrar_camion(id_camion):
        if not id_camion:
            messagebox.showwarning("Faltan Datos", "Debe ingresar el ID del Camión a borrar.")
            return
        if GestorVehicular.borrar_camion(id_camion):
            messagebox.showinfo("Éxito", f"Camión con ID {id_camion} eliminado correctamente.")