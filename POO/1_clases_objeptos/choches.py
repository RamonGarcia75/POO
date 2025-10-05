class Coches:
    def __init__(self, marca: str, color: str, modelo: str, velocidad: int, caballaje: int, plazas: int):
    
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def acelerar(self):

        print(f"El coche {self.marca} está acelerando.")

    def frenar(self):
        
        print(f"El coche {self.marca} está frenando.")

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)

coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

print("Atributos del coche1:")
print(f"Marca: {coche1.marca}")
print(f"Color: {coche1.color}")
print(f"Modelo: {coche1.modelo}")
print(f"Velocidad: {coche1.velocidad} km/h")
print(f"Caballaje: {coche1.caballaje} CV")
print(f"Plazas: {coche1.plazas}")
coche1.acelerar()

print("Atributos del coche2:")
print(f"Marca: {coche2.marca}")
print(f"Color: {coche2.color}")
print(f"Modelo: {coche2.modelo}")
print(f"Velocidad: {coche2.velocidad} km/h")
print(f"Caballaje: {coche2.caballaje} CV")
print(f"Plazas: {coche2.plazas}")
coche2.frenar()

 



coche1=coches()
coche1.marca="VW"
coche1.color="blanco"
coche1