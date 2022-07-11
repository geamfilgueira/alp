#q1: 20

cpf= int(input("digite seu cpf:"))
nome= input("digite seu nome:")
tc= int(input("digite 1 para poupan�a, digite 2 para fundos ou digite 3 para LCI ou LCA:"))
v= int(input("digite o valor investido:"))
m= int(input("digite a quantidade de meses:"))
if tc==1:
    print("o cpf �:", cpf, "o nome �:",nome,"o tipo de conta �:poupan�a", "o rendimento total �:", v+(v*0.5*m))

elif tc==2:
        print("o cpf �:", cpf, "o nome �:",nome,"o tipo de conta �:fundos de renda fixa", "o rendimento total �:", v+(v*1*m))
elif tc==3:
        print("o cpf �:", cpf, "o nome �:",nome,"o tipo de conta �:LCI ou LCA", "o rendimento total �:", v+(v*1.5*m))


#q2: 10 faltou a quantidade dos itens


pedido= int(input("digite 100 para cachorro quente, digite 101 para hamb�rguer ou digite 103 para Bauru completo:"))
pedido2= int(input("digite 100 para cachorro quente, digite 101 para hamb�rguer ou digite 103 para Bauru completo:"))
v1=3
v2=3.50
v3=5

if pedido==100 and pedido2==100:
    print("voc� deve pagar", v1+v1)
elif pedido==100 and pedido2==101:
    print("voc� deve pagar",v1+v2)
elif pedido==100 and pedido2==103:1
    print("voc� deve pagar",v1+v3)
elif pedido==101 and pedido2==101:
        print("voc� deve pagar:",v2+v2)
elif pedido==101 and pedido2==103:
        print("voc� deve pagar:", v2+v3)
elif pedido==103 and pedido2==103:
    print("voc� deve pagar:",v3+v3)


#q3: 15, logica errada do SB

nome= input("digite seu nome:")
horas= int(input("digite o n�mero de horas trabalhadas:"))
dependentes=int(input("digite o n�mero de dependentes:"))
salariob= horas*12
inss= (8.5/100)*salariob
ir=(5/100)*salariob
salariol= salariob+ 40*dependentes - inss - ir
print("Nome:", nome, "o sal�rio bruto �:",salariob, "desconto do inss:",inss, "desconto do ir:",ir, "O sal�rio l�quido vai ser:", salariol)



#q4:20

salariofixo=int(input("digite o sal�rio fixo:"))
carro= int(input("digite a quantidade de carros vendidos:"))
valorvenda= int(input("digite o valor da venda de cada carro:"))
comissao= int(input("digite o valor da comiss�o:"))
cc= comissao*carro
porcentagem= 5/100*valorvenda
salariofinal= salariofixo + cc +porcentagem
print("o sal�rio final �:",salariofinal)












