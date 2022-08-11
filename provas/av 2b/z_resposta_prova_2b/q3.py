#declaracao das variaveis
cont_hab        = 0
quant_masc      = 0
alt_masc        = 0
quant_fem       = 0
alt_fem         = 0
maior_alt       = -1
menor_alt       = 1000
cad_habitante   = "sim"

#coleta dos dados da pesquisa 
while cad_habitante == "sim":
    altura = float(input("Qual a altura do habitante: "))
    sexo = int(input("Qual o sexo (0 - masculino ou 1 - feminino) do habitante: "))
    cont_hab+=1
    cad_habitante = input("Existe mais algum habitante para cadastrar (sim ou não)? ")

    # contando a quantidade de sexos e alturas
    if sexo == 0:
        quant_masc+=1
        alt_masc+=altura
    else:
        quant_fem+=1
        alt_fem+=altura
    
    # encontrando a maior e menor altura
    if altura > maior_alt:
        maior_alt = altura
    elif altura < menor_alt:
        menor_alt = altura
    
#O que se pede:
# 1 - A maior e a menor altura encontradas:
print("Maior altura: ", maior_alt, " - Menor altura: ", menor_alt)

# 2 - A media de altura das mulheres
if quant_fem > 0:
    media_alt_fem = alt_fem/quant_fem
else:
    media_alt_fem = 0
print ("A media de altura das mulheres: ", media_alt_fem)

# 3 - A media de altura da população
media_alt_popu = (alt_masc+alt_fem)/cont_hab
print ("A media de altura da população: ", media_alt_popu)

# 4 - O percentual de homens na população
perc_homens_popu = quant_masc * (100//cont_hab)
print ("O percentual de homens na população: ", perc_homens_popu, "%")