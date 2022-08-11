sexo=0
maior_altura=0
menor_altura=40
dig_alt=0
populacao=0
d=0
f=0
m=0
media_tp=0
soma=0
soma_f=0
media_af=0
pm=0
while d!="não":
    sexo=input("digite seu sexo:")
    dig_alt=float(input("digite sua altura:"))
    populacao=populacao+1
    soma=soma+dig_alt
    media_tp=soma/populacao
    if sexo=="feminino":
        f=f+1
    if sexo=="masculino":
        m=m+1
    soma_f=soma_f+f
    media_af=soma_f/f
    if maior_altura<=dig_alt:
        maior_altura=dig_alt
    if menor_altura>=dig_alt:
        menor_altura=dig_alt
    pm=m/100
    d=input("Ainda existem habitantes para se coletar dados?")
print("A maior altura é:", maior_altura)
print("A menor altura é:", menor_altura)
print("A média da altura da população é:", media_tp)
print("A média de altura das mulheres é:", media_af)


#com erros !