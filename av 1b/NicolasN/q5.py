X = int(input("Valor do lado X: "))
Y = int(input("Valor do lado Y: "))
Z = int(input("Valor do lado Z: "))
if (X<=Y+Z) or (Y<=X+Z) or (Z<=Y+X):
    print ("É um triangulo.")
    if X==Y==Z:
        print ("É equilatero")
    elif X==Y or X==Z or Y==Z:
        print ("É isósceles")
    else:
        print ("É escaleno")
else:
    ("Não é um triangulo")

#20