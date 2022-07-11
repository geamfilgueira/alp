cpf = int (input("Digite seu CPF: "))
nome = input("Digite seu nome: ")
tipcont = input("Digite o tipo de sua conta: ")
valinv = float (input("Digite o valor do investimento: "))
qntmes = int (input("Digite a quantidade de meses investidos: "))
poup = (valinv*0.5/100)*qntmes
frf = (valinv*1/100)*qntmes
lcilca= (valinv*1.5/100)*qntmes
print("Rendimeto total da Poupança (de acordo com o valor inserido): ",poup)
print("Rendimeto total dos Fundos de Renda Fixa (de acordo com o valor inserido): ",frf)
print("Rendimeto total dos LCI ou LCA (de acordo com o valor inserido): ", lcilca)
print("Dados do cliente: ")
print("Nome: ", nome)
print("CPF: ", cpf )
#Aluno: Jessé Leandro Dias, Turma: 1º ano Informática, Integrado.

# Faltou utilizar a estrutura condicional
# 15 