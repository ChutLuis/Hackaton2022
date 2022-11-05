N = int(input("Ingrese el numero total: "))
x= int(input("Ingrese el primer numero para la suma: "))
y= int(input("Ingrese el segundo numero para la suma: "))

aux = x + y
if aux == N :
    numAvellanasx = bin(x).count("1")
    numAvellanasy = bin(y).count("1")
    print("La abuela le dará " + str(numAvellanasx+numAvellanasy) + " Avellanas ")
else:
    print("La suma de los Numeros x e y no es N")