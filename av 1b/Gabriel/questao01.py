#aluno: Gabriel Kleber da Silva Batista
cpf = input('Digite seu cpf: ')
nome = input('Digite seu nome: ')
print('''Contas:
[ 1 ]Poupanca;
[ 2 ]Fundos de renda fixa;
[ 3 ]LCI ou LCA''')
conta = int(input('Digite a conta qual conta você quer: '))
valor = float(input('Digite o valor do investido: R$'))
meses = int(input('digite a quantidade de meses: '))
if conta == 1:
    rm = valor * 0.5 / 100
    vf = rm * meses + valor
    print('Olá {} de cpf {}, o rendimento mensal é de R${:.2f} e o valor final é de R${:.2f}'.format(nome, cpf, rm, vf))
elif conta == 2:
    rm = valor * 1 / 100
    vf = rm * meses + valor
    print('Olá {} de cpf {}, o rendimento mensal é de R${:.2f} e o valor final é de R${:.2f}'.format(nome, cpf, rm, vf))
elif conta == 3:
    rm = valor * 1.5 / 100
    vf = rm * meses + valor
    print('Olá {} de cpf {}, o rendimento mensal é de R${:.2f} e o valor final é de R${:.2f}'.format(nome, cpf, rm, vf))
else:
    print('número invalido!')
