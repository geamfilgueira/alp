m = 0
f = 0
resposta = ''
while resposta != 'nao':
    alt = float(input('digite a altura: '))
    sexo = str(input('digite o sexo f/m: '))
    altmax = 0
    m= 0
    f= 0
    altmax = altmax + alt
    if sexo == "m":
        m = m + 1
    elif sexo == "f":
        f = f + 1
    else:
        print("sexo nao identificado")
    resposta = str(input('quer continuar? sim/nao'))
print ("resultados")
print ("homens: {} mulheres: {}".format(m,f))
print('media de altura: ', altmax/(f+m))

# considerei 10 pontos
