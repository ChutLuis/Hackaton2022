def comparacionCadena(strOriginal, strScambled):
    return strOriginal == strScambled

strOriginal = input("Ingresa la cadena: ")
strScrambled = input("Ingresa la cadena a comparar: ")

listOriginal = list(strOriginal)
listScrambled = list(strScrambled)

listOriginal.sort()
listScrambled.sort()

print(listOriginal)
print(listScrambled)

def comparacionCadena(strOriginal, strScambled):
    return strOriginal == strScambled
    
print(comparacionCadena(listOriginal,listScrambled))