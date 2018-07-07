frase = input("Dime la frase que quieres que analice:\n")
frase_palabras = frase.split()
print(frase_palabras)
palabras = dict()
for palabra in frase_palabras:
    if palabra.lower() in palabras:
        palabras[palabra.lower()] += 1
    else:
        palabras[palabra.lower()] = 1

for clave in palabras:
    print("La palabra {} aparece {} veces".format(clave,palabras[clave]))
