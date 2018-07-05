frase = input("Escriba la frase que quiere saber cuantas vocales y consonantes tiene?\n")
n_consonantes = 0
n_vocales = 0
vocales = ["a","e","i","o","u"]
for letra in  frase:
    if letra in vocales:
        n_vocales +=1
    else:
        n_consonantes +=1

print("La frase tiene {} consonantes y {} vocales".format(n_consonantes,n_vocales))
