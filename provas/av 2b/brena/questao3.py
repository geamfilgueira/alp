maior=0
menor=10000
soma=0
mdf=0
mdm=0
hm=0
alt=0
i=1
while i != "nao":
    sexo=str(input("digite o seu sexo f ou m; "))
    alt=float(input("digite sua aluna; "))
    soma=soma+1
    if sexo=="f":
        mdf=1
    elif sexo== "m":
        mdm=1
    if alt >maior:
        maior=alt
    elif alt<menor:
        menor=alt
    alt=alt+alt
    i=str(input("se quiser para digite nao "))
print("a maior atura eh; " , maior , "a menor altura eh" , menor , "a media da altura das mulheres eh;" ,alt/soma , "o pensentual de humes e de; " , (mdm*soma)/100 )

#considerei 20
