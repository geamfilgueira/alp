#questão 04
salariofixo = float (input("Digite seu salário fixo de um determinado mês: "))
dinporcarrovendido = float (input("Digite quanto você recebe por cada carro vendido: "))
carrovendidos = int(input("Digite quantos carros você vendeu: "))
comissaofixa = dinporcarrovendido*carrovendidos
comissaocomdesconto = (5/100)*comissaofixa
salariototal = salariofixo + comissaofixa + comissaocomdesconto
print ("O funcionário vendeu essa quantidade de carros", carrovendidos)
print ("O valor total de suas vendas foi: ", comissaofixa)
print ("O salário fixo do funcionário é de: ", salariofixo)
print ("O funcionário recebe por cada carro vendido", dinporcarrovendido )
print ("O salário final do funcionário foi de: ", salariototal )



# 20 pontos