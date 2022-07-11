nc = int(input("Digite o num de carros vendidos: "))
vt = float(input("Digite o valor total das vendas: "))
sl = float(input("Digite o seu salario: "))
vcv = float(input("Digite o valor por carro vendido: "))
#comissao por carro vendido
ccv = (vt*5)/100;
sf = sl + ccv + (vcv*nc)
print ("Seu salario final eh ", sf)