import os
os.system("cls")

class Coches:

    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    #Valores Iniciales
    _marca=""
    _color=""
    _modelo=""
    _velocidad=0
    _caballaje=0
    _plazas=0

#Crear los metodos setters y getters, estos modelos son importantes y necesarios
# en todas las clases que el programador interactue con los valores de los atributos a traves
# de estos metodos digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar
# un valor (set) a un atributo en particular de a clase a traves de un objeto
# Los metodos get siepre regresan valor, es decir el valor de la propiedad a traves del return
# Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def Marca(self):
        return self._marca
    
    def Marca(self,_marca):
        self._marca=_marca

    def Color(self):
        return self._color
    
    def Color(self,_color):
        self._color=_color

    def Modelo(self):
        return self._modelo
    
    def Modelo(self,_modelo):
        self._modelo=_modelo
    
    def Velocidad(self):
        return self._velocidad
    
    def Velocidad(self,_velocidad):
        self._velocidad=_velocidad
    
    def Caballaje(self):
        return self._caballaje
    
    def Caballaje(self,_caballaje):
        self._caballaje=_caballaje
    
    def Plazas(self):
        return self._plazas

    def Plazas(self,_plazas):
        self._plazas=_plazas

#Metodos o acciobes o funciones que hace el objeto
    def acelerar(self):
        return"estoy acelerando el coche"
        pass

    def frenar(self):
        return"estoy parando"
        pass


class Camiones(Coches):
    def__ini_(self,marca,color,modelo,velocidad,cballaje,plazas)
    super().__int__(self,marca,color,modelo,velocidad,cballaje,plazas):
    self.__eje=eje
    sefl.__capasidadCarga=capasidadCarga


    #metodso set y get 
    @property
    def eje(self,eje):

    @property
    def capasidadCarga  




#Crea un objeto o instancia de la clase Coches
coche1=Coches()
#Utiliza los metodos set para darle valores a las propiedades o atributos del objeto coche1
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
#Utiliza los metodos get para obtener los valores de las propiedades o atributos del objeto coche1
print(f'''
Marca: {coche1.getMarca()}
Color: {coche1.getColor()}
Modelo: {coche1.getModelo()}
Velocidad: {coche1.getVelocidad()}
Caballaje: {coche1.getCaballaje()}
Plazas: {coche1.getPlazas()}
''')

coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f'''
Marca: {coche2.getMarca()}  
Color: {coche2.getColor()}
Modelo: {coche2.getModelo()}
Velocidad: {coche2.getVelocidad()}
Caballaje: {coche2.getCaballaje()}
Plazas: {coche2.getPlazas()}
''') 
