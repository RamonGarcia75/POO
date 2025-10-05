#print("super calculadora")
#print(int("ingrese un{valorentero1}"))
#print(int("ingrese{otrovalor entero2}"))

#__init__(sum)
#({valorentero1}+{valorentero2}=sum valores)
#return (sum valores)

#__init__(min)
#({valorentero1}-{valorentero2}=min valores)
#return (min valores)

#__init__(multiplication)
#({valorentero1}*{valorentero2}=multiplication valores)
#return (multiplication valores)

#__init__(divicion)
#({valorentero1}/{valorentero2}=divicion valores)
#return (divicion valores)

#print("¿que valor desea ver?")

#print(f"{sum=1}{resta=2}{multiplication=3}{divicion=4}")

class calculadora:
    def __init__(self):
        self._numero1=int(input("numero #1:"))
        self._numero2=int(input("numero #2:"))
    
    @property
    def numero1(self):
        return self.numero1
    
    @numero2.setter
    def sumar(self):
        sumar=self._numero1+self._numero2

    def restar(self):
        restar=self._numero1-self._numero2

    def multiplicar(self):
        multiplicar=self._numero1*self._numero2

    def divicion(self):
        divicion=self._numero1/self._numero2


operacion=calculadora()
print(f"{operacion.numero1operacion.sumar())
print(operacion.restar())
print(operacion.multiplicar())
print(operacion.divicion())

    

