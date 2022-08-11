p = input("diga sim se for pesquisar")
hab = 0
al_f = 0
al_m = 0

while p != "nao":
    while hab != "sim" :
        al = float(input("digite uma altura: "))
        sx = input("diga o seu sexo (m/f): ")
        hab = hab + 1
        al_f = al_f + al
        al_m = al / hab
        while sx == m:
            m += 1
            print(m)
            p = (input("deseja continuar a pesquisa (sim ou nao)"))
if sx == f:
    print("a media da altura das mulheres e,", al_f / sx)

print("a altura media da populacao e,", al_m)

#erro





