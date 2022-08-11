x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
z = int(input("digite o valor de z: "))
if x+y > z and x+z>y and z+y>x:
    if x==y==z:
        print("triangulo equiulatero")
    elif x==y or x==z or z==y:
        print ("triangulo isosceles")
    elif x != y != z:
        print ("triangulo escaleno")

# 20