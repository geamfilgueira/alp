#Maria Cec�lia de Morais Pereira Soares

#1- faltou exibir os valores - 15
cpf= input("Digite seu cpf:")
Nome= input("Digite seu nome:")
Tc= input("Digite o tipo de conta:")
Vi= float(input("Digite o valor investido:"))
Meses= int(input("Digite a quantidade de meses:"))
Tc1= ((Vi*0.5)*Meses)/100
Tc2= ((Vi*1.0)*Meses)/100
Tc3= ((Vi*1.5)*Meses)/100

if (Tc1):
    print("Conta poupan�a")
elif (Tc2):
    print("Conta Fundos de Renda Fixa")
elif (Tc3):
    print("Conta LCI ou LCA")

#------------------------------------------------------------------------
#3- logica errada 10
Nome= input("Digite o nome:")
Numh= int(input("Digite o n�mero de horas trabalhadas:"))
Numd= int(input("Digite o n�mero de dependentes de um funcion�rios:"))
Sb= ((12*Numh)+(40*Numd))
Vdesc1= (Sb*8.5)/100
Vdesc2= (Sb*5)/100
Sl= Sb + Vdesc1 + Vdesc2

print("O nome �:",Nome)
print("O sal�rio bruto:" ,Sb,)
print("O valor de desconto do INSS �:", Vdesc1)
print("O valor de desconto do IR � :" ,Vdesc2)
print("O sal�rio bruto � :", Sl)

#--------------------------------------------------------------------------
#4- 20 
A= int(input("Digite o n�meros de carros por ele vendidos:"))
B= float(input("Digite o valor total de suas vendas:"))
C= float(input("Digite o sal�rio fixo:"))
D= float(input("Digite o valor que ele recebe por carro:"))
Vv= (B*5)/100
Sf= C + D + Vv

print("O sal�rio final � de:",Sf)

#--------------------------------------------------------------------------
#5- 20
X= int(input("Digite o valor de x:"))
Y= int(input("Digite o valor y:"))
Z= int(input("Digite o valor de z:"))

if X == Y and Y == Z and Z == X:
    print("Tri�ngulo equil�tero")
elif X == Y or Y == Z :
    print("Tri�ngulo is�sceles")
elif X != Y  or Y != Z or Z != X:
    print("Tri�ngulo escaleno")
