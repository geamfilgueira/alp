
maior = -100
menor = 50000

while True:
    cd_tipo = input("dia o seu codigo residencial, comercial, industrial ")
    n_cons = int(input("digite seu numero: "))

    quant_resid = 0
    quant_comer = 0
    quant_indus = 0

    if n_cons == 0:
        break
    if maior < preco_kwh:
        maior = preco_kwh
    elif menor > preco_kwh:
        menor = preco_kwh

    if cd_tipo == "residencial":
        preco_kwh = int(input("diga o preco consumido de kwh: "))
        n_cons = int(input("digite seu numero: "))
        q_cons_mes = int(input("diga o preco consumido de kwh durante o mes: "))
        quant_resid = q_cons_mes + quant_resid
    elif cd_tipo == "comercial":
        preco_kwh = int(input("diga o preco consumido de kwh: "))
        n_cons = int(input("digite seu numero: "))
        q_cons_mes = int(input("diga o preco consumido de kwh durante o mes: "))
        quant_comer = q_cons_mes + quant_comer
    elif cd_tipo == "industrial":
        preco_kwh = int(input("diga o preco consumido de kwh: "))
        n_cons = int(input("digite seu numero: "))
        q_cons_mes = int(input("diga o preco consumido de kwh durante o mes: "))
        quant_indus = q_cons_mes + quant_indus
    media = q_cons_mes / preco_kwh
print("o maior consumo e, ", maior, "e o menor e, ", menor)
print("o total de consumo e para residencial e ,", quant_resid)
print("o total de consumo e para comercial e ,", quant_comer)
print("o total de consumo e para industrial e ,", quant_indus)

#solucao errada 

