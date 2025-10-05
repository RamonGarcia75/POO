#instanciar los objeptos para posteriormente
from coches import Coches
#import coches
    
num_coches=int(input("cuantos coches desea?"))

for i in range(0,num_coches):
    print(f"dtos de coche {i+1}")
    marca=input("ingresa la marca").upper()
    color=input("ingresa la color").upper()
    modelo=input("ingresa la modelo").upper()
    velocidad=int(input("ingresa la velocidad"))
    potencia=int(input("ingresa la potencia"))
    plazas=int(input("ingresa la plazas"))

coche1=coches(marca,color,modelo,velocidad,potencia,plazas)

print(f"datos del vehiculo /n marca:{coche1.marca} /n color:{coche1.color}")

print({coche1.acelerar()})
coche=coches.Coches()

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
