#programa un codigo que usando el metodo replace de las string que sustituya las claves de mi string inicia por los valores en orden de una lista
valores_a_sustituir = [1,2, "hola", "adios"]
string_a_cambiar = "Hola, numero {},numero {}, {} y {}"
print(string_a_cambiar)
for item in valores_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("{}",str(item),1)

print(valores_a_sustituir)
print(string_a_cambiar)