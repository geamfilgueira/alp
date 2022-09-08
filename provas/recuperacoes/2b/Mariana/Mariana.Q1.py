maior=0
menor=999
soma=0
comercial=0
residencial=0
industrial=0
i=0
while True:
    i+=1
    preco=float (input("digite o preco"))
    num=int (input("digite o numero do consumidor"))
    qnt = int(input("digite a qn de kmw consumidos"))
    soma= soma+qnt
    cod=str(input("digite seu codigo, residencial, comercial, indusrial"))
    if num == 0:
        break
    if qnt > maior:
        maior = qnt
    if qnt < menor:
        menor = qnt
    if cod == "comercial":
        comercial=comercial+qnt
    elif  cod == "residencial":
        residencial=residencial+qnt
    elif  cod == "industrial":
        industrial=industrial+qnt

print("O maior consumo foi:", maior)
print("O menor consumo foi:", menor)
print("O total de consumo dos residenciais foi:", residencial)
print("O total de consumo dos comerciais foi:", comercial)
print("O total de consumo dos industriais foi:",industrial)
print("A media de consumo foi:", soma/i)
