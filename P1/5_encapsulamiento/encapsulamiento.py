#es unn pilar de la poo qie permiy¿te indicar cual es ela manerra de como poder utilizar los atribitos y metodos de una clase a la hora de usar objeptos o en herencia

class Clase:
    atributo_publico="soy un atributo publico "
    atributo_protejido="soy un atributo protejido"
    __atributo_privado="soy un atributo privado" 


    def __init__(self,color,tamano):
        self.__color=color
        self.__tamano=tamano


    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamano(self,tamano):
        return self.__tamano
    
    @tamano.setter
    def tamano(self,tamano):
        self.__tamano=tamano

    @property
    def atributo_publico(self):
        return self.atributo_publico
    
    @atributo_publico.setter
    def atributo_publico(self,atributo_publico):
        self.atributo_publico=atributo_publico

    @property
    def atributo_protejido(self):
        return self.atributo_protejido
    
    @atributo_protejido.setter
    def atributo_protejido(self,atributo_protejido):
        self.atributo_protejido=atributo_protejido


    def getAtributoPrivado(self):
        return self.__atributo_privado

    @property
    def atributo_privado(self):
        return self.atributo_privado
    
    @atributo_privado.setter
    def atributo_provado(self,atributo_privado):
        self.atributo_privado=atributo_privado




#utilizar clase 

objpeto=Clase("rojo","grande")
#print(objpeto.atributo_publico)
#print(objpeto.atributo_protejido)
print(objpeto.getAtributoPrivado)
print()

