class calculadora:
    def __init__(self,numero1,numero2):
        self.numero1= numero1
        self.numero2 = numero2
    def suma(self):
        suma = self.numero1 + self.numero2
        return suma
    def resta(self):
        resta = self.numero1 - self.numero2
        return resta
    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        return resultado
    def division(self):
        resultado=self.numero1/self.numero2
        return resultado

numero1 = int(input("Dime el primer numero\n"))
numero2 = int(input("Dime el segundo numero\n"))
while True:
    operacion = input("Dime que operacion deseas realizar: suma, resta, multiplicacion,division\n")
    if operacion.lower() == "suma" or operacion.lower() =="resta" or operacion.lower() == "multiplicacion" or operacion.lower() =="division":
        break
    else:
        print("No has escogido una operacion de las propuestas")

calculadora = calculadora(numero1,numero2)
if operacion == "suma":
    suma = calculadora.suma()
    print("El resultado es: {}".format(suma))
elif operacion == "resta":
    resta = calculadora.resta()
    print("El resultado es: {}".format(resta))
elif operacion == "multiplicacion":
    multiplicacion = calculadora.multiplicacion()
    print("El resultado es: {}".format(multiplicacion))
elif operacion == "division":
    division = calculadora.division()
    print("El resultado es: {}".format(division))