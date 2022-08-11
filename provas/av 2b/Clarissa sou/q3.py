alt=0
menor_alt=300
maior_alt=-1
sexo=0
fem=0
masc=0
media_mulheres=0
soma_população=0
alt_mulheres=0
media_população=0


while alt>=0:

    alt=int(input("digite a altura em cm: se quiser parar o codigo digite um número negativo:"))
    if alt>=0:
        soma_população=soma_população+alt
        sexo=int(input("digite 0 para masc e 1 para f:"))
        if sexo==0:
            masc=masc+1

            print("A quantidade de pessoas do sexo masculino é:",masc)
        if sexo==1:
            fem=fem+1
            alt_mulheres=alt_mulheres+alt
            print("A quantidade de pessoas do sexo feminino é:",fem, "A soma das alturas das mulheres é:", alt_mulheres)

        if alt>maior_alt:
            maior_alt=alt
            print("A maior altura é", maior_alt)
        if alt<menor_alt and alt<maior_alt:
            menor_alt=alt
            print("A menor altura é:", menor_alt)




if alt_mulheres >0 and fem>0:
    media_mulheres=alt_mulheres/fem
media_população= soma_população/(fem+masc)

print("A maior altura é:", maior_alt, "A menor altura é:", menor_alt, "A média das alturas das mulheres é:", media_mulheres, "A média de altura da população é:", media_população, "A quantidade de homens é:", masc)

# considerei 25 pontos