

cpf = int(input( "DIGITE O NUMERO DO SEU CPF "))
nome = input("DIGITE O SEU NOME ")
tp = input( "DIGITE O TIPO DE CONTA ")
inv = int(input( "VALOR INVESTIDO "))
quantM = int(input( "QUANTIDADE DE MESES DO INVESTIMENTO "))

ppc = (inv * quantM * 0,5)
FRF = (inv * quantM * 1)
LCILCA = (inv * quantM * 1,5)

poupanca = print(cpf, nome, tp , inv , quantM , ppc )

fundosderendafixa = print(cpf, nome, tp, inv, quantM, FRF )

LCIouLCA = print(cpf, nome, tp , inv , quantM , LCILCA )

# logica errada
# 5
