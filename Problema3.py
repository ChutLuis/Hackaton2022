
strOriginal = input("Ingresa la cadena: ")
strComparar = input("Ingresa la cadena a comparar: ")

listOriginal = list(strOriginal)
listComparar = list(strComparar)

aux = ""
if len(listOriginal) == len(listComparar):
    for i in range(len(listOriginal)):
        if(listComparar[i] == listOriginal[i]):
            aux += listComparar[i]

print(aux)
