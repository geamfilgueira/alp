fim = ''
maior = 0
maioraltura = 100
menor = 0
menoraltura = -1000
mulher = 0
media = 0
m = 0
mp = 0
perc = 0


while fim != sim:
    alturamulher = float(input("digite altura da mulher:"))
    alturahomem = float(input("digite a altura do homem:"))
    populacao = int(input("populaçao de patos :"))
    sexofeminino = int(input("digite a quantidade:"))
    sexomasculino = int(input("digite a quantidade :"))

    if  maioraltura > menoraltura :
        maior = maior + maioraltura
        print(maior)
    else:
        print(menor)
    if alturamulher > 0:
        media = sexofeminino/alturamulher
        print(media)
    if populacao > 0:
        me = alturamulher+alturahomem
        mp = me /populacao
        print(mp)
    if sexomasculino > 0:
        perc = mp/sexomasculino
        print(perc)

print("maior altura ",maior,"menor altura",menor)
print("a media de altura das mulheres",media)
print("a media de altura da populacao",mp)
print("o percentual de homens na populaçao",perc)


#questão com erro.. considerei 10 pontos