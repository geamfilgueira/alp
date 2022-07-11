#Myrelle Ferreira da Nobrega Moreira
#questao 4
cv = int(input("digite o numero de carros vendidos: "))
vt = float(input("digite o valor total de vendas: "))
sf = float(input("digite seu salario fixo: "))
vc = float(input("digite o valor por carro: "))
cf = int(input("digite sua comissao fixa: "))
salario_final = sf+(cf*cv)+vt*(5/100)
print("meu salario final eh: ", salario_final)