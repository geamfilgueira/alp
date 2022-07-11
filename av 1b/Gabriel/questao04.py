#aluno: Gabriel Kleber da Silva Batista
s = float(input('digite seu salario: '))
vv = float(input('digite o valor total das vendas: R$'))
v = float(input('valor por carro vendido: R$'))
n = int(input('numero de vendas: '))
sf = s + v * n + (vv * 5 / 100)
print('R${:.2f}'.format(sf))
# certo 20