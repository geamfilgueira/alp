x = int(input("Digite um valor para o lado x: "))
y = int(input("Digite um valor para o lado y: "))
z = int(input("Digite um valor para o lado z: "))

if x < y + z and y < x + z and z < x + y:
    if x == y == z: 
        print ("Equilátero!")
    elif x == y or y == z or x == z:
        print ("Isosceles") 
    elif x != y != z:
        print ("Escaleno")
else:
    print("nao eh triangulo")