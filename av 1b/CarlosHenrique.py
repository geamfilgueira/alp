Nome = input("Insira o nome do cliente: ")
Cpf = input ("Insira o Cpf do cliente: ")
Conta = input ("Tipo da conta: ")
Investimento = float (input("Valor do investimento: "))
Meses = int(input("Quatidade de meses do investimento: "))
#CarlosHenriquedaSilva

Poupanca = 0,5
FundosdeRenda = 1
LCIouLCA = 1,5

if Poupanca :
    print((Investimento/0,5)*Meses )
elif FundosdeRenda:
    print((20,00/1)*4)
else:
    print(" Cabou")


Produto1 = int(input("Código 1"  ))
Produto2 = int(input("Código 2" ))

Cachorro = 3,00
Hamburger = 3,50
Bauru  = 5,00

print("Codigo 1: ", Produto1, "Codigo 2: ", Produto2, "Valor:", Cachorro + Bauru  )


Nome = "jonas"
Horas = 3
Dependentes = 2

PorHora = 12
De = 40
a = 8,5
b = 5

SB = (12 * 3) + (40 * 2)
Desconto = 116/5 + 116,00/8,5
SalarioL = SB - Desconto

print("Nome: ", Nome, "Horas trabalhadas: ", Horas, "Numeros de dependentes: ", Dependentes, "Salario bruto: ", SB, "Descontos: ", Desconto, "Salrio liquido: ", SalarioL )


NC = int(input("Número de carros vendidos: "))
VTS = float(input("Valor total de vendas: "))
SL = float(input("Salario fixo: "))
VPC = float(input("VAlor por carros vendidos: "))

BV = (VTS / 5,0) * NC

print(BV + SL +VPC)

Lado1 = int(input("Comprimento1: "))
Lado2 = int(input("Comprimento2: "))
Lado3 = int(input("Comprimento3: "))

if Lado1==Lado2==Lado3:
    print("Equilatero")
elif Lado1==Lado2=/Lado3:
    print("Isoceles")
else Lado1=/Lado2=/Lado3:
   print("Escaleno")



