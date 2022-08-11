
masc = 0
fem = 1
maior = -1000
menor = 1000
media1 = 0
media2 = 0
soma1 = 0
quant1 = 0
soma0 = 0
quant = 0
mediapopu = 0
sair = " "
populacao = 0
while sair != 'sair':
    populacao = int(input("digite 0 para masculino ou 1 para feminino"))
    if populacao == 1:
        altura1 = int(input("digite a altura: "))
        idade = int(input("digite sua idade: "))
        soma1 = soma1 + altura1
        quant1 = quant1 + 1
    elif populacao == 0 :
        altura0 = int(input("digite a altura: "))
        idade = int(input("digite sua idade: "))
        soma0 = soma0 + altura0
        quant =quant + 1

    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade
    sair = input("digite sair ou continuar ;")
media1 = soma1/quant1
media2 = soma0/quant
mediapopu = media1/media2
media1 = soma1/quant1
media2 = soma0/quant
totalaltura = altura1 + altura0
mediapopu = totalaltura/(quant1 + quant)

print("a maior idade eh", maior, "e a menor eh", menor, "a media de altura das mulheres eh:", media1, "a media de altura dos homens eh:", media2, "a media da população eh", mediapopu, "a quantidade de homens eh",quant)



#com erros considerei 15 pontos