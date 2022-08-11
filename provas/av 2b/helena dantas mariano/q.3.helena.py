fim = " "

total = 0

maior = -1000
menor = 1000

soma = 0
soma2 = 0

fem = 0
mas = 0


while fim != 'sair':
    alt = float(input("digite sua altura: "))
    alt2 = float(input("repita apenas a altura das mulheres: "))
    sexo = str(input("digite seu sexo: "))
    soma += alt
    soma2 += alt2

    if alt > maior:
        maior = alt

    elif alt < menor:
        menor = alt

    elif sexo == "F":
        fem = sexo

    elif sexo == "M":
        mas = sexo

    total += 1

    fim = int(input('''digite se deseja sair:
    continuar
    sair '''))

print ("maior altura: ", maior)
print ("menor altura: ", menor)
print ("media da população: ", soma/total)
print ("media da altura das mulheres: ", soma2/fem)
print ("quantidade de homens: ", mas)



#15 pontos