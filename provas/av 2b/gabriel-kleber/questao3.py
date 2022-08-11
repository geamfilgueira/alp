maior_altura = 0
menor_altura = 1000
med_mulheres = 0
med_alturas = 0
per_hom = 0
mulheres = 0
hab = 0
while True:
    exi = str(input('Tem mais algum habitante? ')).upper()
    if exi == 'NAO' or exi == 'N' or exi == 'NÃO':
        break
    hab += 1
    print('[ 0 ] Masculino')
    print('[ 1 ] Feminino')
    sex = int(input('Qual o sexo: '))
    if sex == 1:
        altura = float(input('Digite sua altura em metros:m '))
        med_mulheres += altura
        if altura < menor_altura:
            menor_altura = altura
        if altura > maior_altura:
            maior_altura = altura
        med_alturas += altura
        mulheres += 1
    elif sex == 0:
        altura = float(input('Digite sua altura em metros:m '))
        if altura < menor_altura:
            menor_altura = altura
        if altura > maior_altura:
            maior_altura = altura
        per_hom += 1
        med_alturas += altura
if mulheres > 0:
    mediamulh = med_mulheres/mulheres
    print('A média de altura das mulheres é de {:.2f}m'.format(mediamulh))
media = med_alturas/hab
mediahom = per_hom * (100/hab)
print('o Percentual de homens é de {}%'.format(mediahom))
print('A média de altura da população é de {:.2f}m'.format(media))
print('A maior altura é de {:.2f}m'.format(maior_altura))
print('A menor altura é de {:.2f}m'.format(menor_altura))
