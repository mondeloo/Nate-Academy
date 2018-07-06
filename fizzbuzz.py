#dada una lista de enteros vamos a sustituir los multiplos de 3 por un Fizz y los de 5 por un Buzz, los que sean multiplos de ambos por FizzBuzz
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,14,20,15,30,60,70]
numeros_final = []
for numero in numeros:
    modulus_three = numero%3
    modulus_five = numero%5
    if modulus_three + modulus_five == 0:
        numeros_final.append("FizzBuzz")
    elif modulus_five == 0:
        numeros_final.append("Buzz")
    elif modulus_three == 0:
        numeros_final.append("Fizz")
    else:
        numeros_final.append(numero)

print(numeros)
print(numeros_final)
