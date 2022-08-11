import string

MaiorAF = -1
MenorAF = 4000
MaiorAH = -1
MenorAH = 4000
Maioraltura = -1
Menoraltura = 4000
MédiadAdasMulheres = (MaiorAF + MenorAF)/2
QdM = 0
QdH = 0
PercentualH= QdH
MédiadAdaPopulação = ((MaiorAF + MenorAF) + (MaiorAH + MenorAH)/2

while tem_mais == "Não":
    Habitante = input("Digite seu nome:")
    Sexo = input("Seu sexu? M ou H?")
    if Sexo == M:
        AlturaF = int(input("Sua altura amigo(a): ")
    elif Sexo == H:
        AlturaH = int(input("Sua altura amigo(a): ")

    if Sexo == M:
        QdM = QdM + 1
    elif Sexo == H:
        QdH = QdH + 1


    if MaiorAF < AlturaF:
      MaiorAF = AlturaF

    if MenorAF > AlturaF:
        MenorAF = AlturaF:

    if MaiorAF < AlturaH:
      MaiorAF = AlturaH

    if MenorAH > AlturaH:
        MenorAH = AlturaH:

    tem_mais = string(input("Sim ou não?"))

print("A maior altura eh", MaiorAF, "A menor eh", MenorAF)
print("A média de altura das mulheres eh: ", MédiadAdasMulheres)
print("A média de altura da população eh: ", MédiadAdaPopulação)
print("Quantidade de homens: ", QdH)

# considerei 10 pontos