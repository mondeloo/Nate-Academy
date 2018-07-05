lista_compra =[]
quiere = input("Quieres escribir una lista de la compra?(Si/No)\n")

if quiere.lower() == "si":
    while True:
        elemento = input("Que quiere comprar?(Escriba nada para salir)\n")
        if elemento.lower() == "nada":
            break
        else:
            lista_compra.append(elemento)

long = len(lista_compra)
if long > 0:
    print("Tienes que comprar:")
    m = 0
    while long > 0:
        print(lista_compra[m])
        m += 1
        long -= 1


