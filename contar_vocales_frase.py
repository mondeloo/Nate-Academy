frase = input("Escriba la frase que quiere saber cuantas vocales y consonantes tiene?\n")
consonantes = 0
vocales = 0
for letra in  frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales +=1
    else:
        consonantes +=1

print("La frase tiene {} consonantes y {} vocales".format(consonantes,vocales))
