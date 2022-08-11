min = 888
# Menor altura
max = 0
# Maior altura
am = 0
# Altura das mulheres
m = 0
# Quantidade de mulheres
h = 0
# Quantidade de homens
pessoa = 0

while pessoa != "ACABOU":
# Eu sei que esse acabou é redundante já que já existe um break, mas tinha que colocar alguma condição no while.
    pessoa = input ("Sexo M ou H: ").upper ()
    if pessoa == "ACABOU":
        break
    alt = float (input("Digite sua altura: "))
    if pessoa == "M":
        m = m + 1
        am = am + alt
    elif pessoa == "H":
        h = h + 1
    if alt > max:
        max = alt
    if alt < min:
        min = alt
if m == 0:
# Se não existir mulheres no final de tudo vai ser somado 1 para que as divisões ocorram.
    m = m + 1
    print ("A média de altura das mulheres é: ", am/m)
# Era aqui onde o bendito dava erro.
    print ("A maior altura é: ", max)
    print ("A menor altura é: ", min)
    print ("A porcentagem de homens é de: ", h/(h+m-1)*100, "%")
# Compensei o que foi adicionado p/ não dar nada errado na linha 34 e 36
    print ("A população é de ", m-1 + h, "habitantes")
else:
    print ("A maior altura é: ", max)
    print ("A menor altura é: ", min)
    print ("A média de altura das mulheres é: ", am/m)
    print ("A porcentagem de homens é de: ", h/(h+m)*100, "%")
    print ("A população é de ", m + h, "habitantes")



#25 pontos