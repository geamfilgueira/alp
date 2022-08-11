fim = ""
total_p = 0
soma_a = 0
total_s_1 = 0
total_s_0 = 0
soma_a_1 = 0
media_a_1 = 0
media_a_p = 0
maior_a = 3.0
menor_a = -1
while fim != "sim":
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo: ")
    soma_a_1 = soma_a_1 + altura
    soma_a = soma_a + altura
    soma_a_1 = soma_a_1 + altura
    if altura > maior_a:
        maior_a = altura
    elif altura < menor_a:
        menor_a = altura
        total_p = total_p + 1
        if sexo == "0":
            total_s_0 = total_s_0 + 1
        else:
            total_s_1 = total_s_1 + 1
            fim = input("Tem mais habitantes, sim ou não: ")

print("A media de altura da população é:", soma_a/total_p)
print("A media de altura das mulheres é:", soma_a_1/total_s_1)
print("A maior altura é;", maior_a)
print("A menor altura é", menor_a)


# errado