#aluno: Gabriel Kleber da Silva Batista
print('''Cardápio:
[ 100 ] Cachorro quente
[ 101 ] Hambúguer
[ 103 ] Bauru Completo
Caso não queira nada digite [ 000 ]''')
q1 = int(input('digite um código: '))
if q1 == 100:
    p1 = int(input('Quantos cachorros quentes você vai querer: '))
    p2 = 3.00 * p1
elif q1 == 101:
    p1 = int(input('Quantos Hambúgueres você vai querer: '))
    p2 = 3.50 * p1
elif q1 == 103:
    p1 = int(input('Quantos baurus você vai querer: '))
    p2 = 5.00 * p1
elif q1 == 000:
    print('obrigado pela preferencia!')

q2 = int(input('digite um código: '))
if q2 == 100:
    p1 = int(input('Quantos cachorros quentes você vai querer: '))
    p3 = 3.00 * p1
elif q2 == 101:
    p1 = int(input('Quantos Hambúgueres você vai querer: '))
    p3 = 3.50 * p1
elif q2 == 103:
    p1 = int(input('Quantos baurus você vai querer: '))
    p3 = 5.00 * p1
elif q2 == 000:
    print('obrigado pela preferencia!')

q3 = int(input('digite um código: '))
if q3 == 100:
    p1 = int(input('Quantos cachorros quentes você vai querer: '))
    p4 = 3.00 * p1
elif q3 == 101:
    p1 = int(input('Quantos Hambúgueres você vai querer: '))
    p4 = 3.50 * p1
elif q3 == 103:
    p1 = int(input('Quantos baurus você vai querer: '))
    p4 = 5.00 * p1
elif q3 == 000:
    print('obrigado pela preferencia!')
pf = p2 + p3 + p4
print('o preço é de R${:.2f}'.format(pf))

# Solicitou 3 pedidos... só precisava de dois... e declarou as variaveis locais, caso o usuário opte só por sois
# mas irei considerar 15