#questão 01
nome = input("Digite seu nome: ")
cpf = int (input("Digite seu CPF: "))
tipoconta = input ("Digite o tipo da sua conta: ")
valorin = float(input("Digite o valor do seu investimento: "))
mi = int (input("Digite a quantidade de meses do investimento: "))
poupanca = (0.5/100)*valorin
fundosderenda = (1/100)*valorin
lci = (1.5/100)*valorin
redimentototal = (poupanca + fundosderenda + lci)*mi
print ("A sua poupança mensal foi de:", poupanca)
print ("Os seus fundos de renda fixa mensal foi de: ", fundosderenda)
print ("O seu lci mensal foi de: ", lci)
print ("Seu rendimento total foi:", redimentototal)


# 17