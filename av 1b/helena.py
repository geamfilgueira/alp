#\3HELENA DANAS MARIANO
#INFORMAICA INEGRADO


#questao 4: 

salariof = float(input("coloque o seu salario fixo: "))
carros = float(input("coloque a quantidade de carros vendidos: "))
valcar = float(input("o valor que recebe por carro �: "))
valor = float(input("o valor total das vendas foi: "))

print ((carros * valcar * 5/100 ) + salariof + valor)

#questao 5:

x = int(input("digite o comprimento do 1 numero: "))
y = int(input("digite o comprimento do 2 numero: "))
z = int(input("digite o comprimento do 3 numero: "))

if (x == y) and (y == z):
    print ("triangulo equilatero")
elif (x == y) and (x < z + y):
    print ("triangulo isoceles")
else:
    print ("triangulo escaleno")