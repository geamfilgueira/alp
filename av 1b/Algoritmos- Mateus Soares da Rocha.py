#Quest�o 1 20

#Mateus Soares da Rocha Cordeiro - 1
CPF = int(input("Digite seu CPF: "))
nome = input("Digite seu nome: ")
conta = input("Digite o tipo da conta: ")
IV = int(input("Digite o valor investido: "))
ME = int(input("Digite a quantidade de meses: "))
if conta == "Poupan�a":
    print ("Seu redimento total foi de",(IV*ME)*0.5)
elif conta == "Fundos de Renda Fixa":
    print ("Seu redimento total foi de",(IV*ME)*1.0)
elif conta == "LCI" or conta == "LCA":
    print ("Seu redimento total foi de",(IV*ME)*1.5)
else:
    ("Escolha uma conta valida ")

#Quest�o 2 20

#Mateus Soares da Roha Cordeiro - 2
cod1 = input("Digite o codigo do primeiro pedido, digite 100 para cachorro quente, 101 para hamb�rguer ou 102 para um bauru completo: ")
cod2 = input("Digite o codigo do primeiro pedido, digite 100 para cachorro quente, 101 para hamb�rguer ou 102 para um bauru completo(lembresse n�o tem pra quer esolher o mesmo codigo 2 vezes): ")
if cod1 == "100":
    if cod2 == "101":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*3.00+cod2*3.50,"reais")
    elif cod2 == "102":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*3.00+cod2*5.00,"reais")
elif cod1 == "101":
    if cod2 == "100":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*3.50+cod2*3.00,"reais")
    elif cod2 == "102":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*3.50+cod2*5.00,"reais")
elif cod1 == "102":
    if cod2 == "100":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*5.00+cod2*3.00,"reais")
    elif cod2 == "101":
        cod1 = int(input("Digite a quantidade de pedidos para o codigo 1: "))
        cod2 = int(input("Digite a quantidade de pedidos para o codigo 2: "))
        print ("O valor do pedido � de R$",cod1*5.00+cod2*3.50,"reais")
else:
    print("Verifique o n�mero do pedido.")



#Quest�o 3 20

#Mateus Soares da Roha Cordeiro - 3
nome = input("Digite seu nome: ")
hora = int(input("Digite o numero de horas trabalhadas: "))
depe = int(input("Digite o n�mero de dependentes: "))
SB = hora*12+depe*40
inss = SB*0.085
ir = SB*0.05
print ("Seu nome eh",nome,", seu salario bruto � R$",SB,"seu salario tem um desconto de R$",inss,"para o inss e outro de R$",ir,"para o IR")
print ("Seu salario liquido equivale a R$",(SB-inss)-ir)




#Quest�o 4 20

#Mateus Soares da Rocha Cordeiro - 4
Sal = float(input("Digite o valor do Salario: "))
venda = float(input("Digite o valor das vendas: "))
Nc = int(input("Digite o numero de carros: "))
Vc = float(input("Digite o valor a reeber por carro: "))
print ("O salrio final do vendedor � de",Sal+Nc*Vc+venda*0.05)


#Quest�o 5 20


#Mateus Soares da Roha Cordeiro - 5
X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor Y: "))
Z = float(input("Digite o valor de Z: "))
if Z<X+Y or X<Z+Y or Y<X+Z:
    if Z==X==Y:
        print ("Tri�ngulo Equil�tero")
    elif Z==X or Z==Y or Y==X:
        print ("Tri�ngulo Is�celes")
    else:
        print ("Tri�ngulo Escaleno")
else:
    ("N�o formam um tri�ngulo.")