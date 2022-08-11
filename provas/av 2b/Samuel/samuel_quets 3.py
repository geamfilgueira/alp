fim = ""
sex_m = 0
qnt_m = 0
sex_f = 0
qnt_f = 0
alt_f = 0
alt_p = 0
me_alt = 0
me_alt_f = 0
qnt_h = 0
maior_alt = -1
menor_alt = 10000
while fim != 'não':
    alt = float(input("digite sua altura:"))
    if alt >= maior_alt:
        maior_alt = alt
    elif alt <= menor_alt:
        menor_alt = alt
    sex = input("Digite o sexo do habitante:")
    if sex == "f":
        sex_f += 1
        qnt_f += 1
    elif sex == "m":
        sex_m += 1
        qnt_m += 1
    qnt_h = qnt_h + 1
    alt_f = alt_f + sex_f
    alt_p = alt_p + alt
    me_alt_f = alt_f/qnt_f
    me_alt = alt_p/qnt_h
    fim = input("Ainda existem habitantes?")
print("A maior altura eh:", maior_alt )
print("A menor altura eh:", menor_alt)
print("A altura media das mulheres eh:", me_alt_f)
print("A altura media da população eh:", me_alt)
print("O percentual de homens eh de:", qnt_m/qnt_f)

# com erro, mas considerei 15 pontos.