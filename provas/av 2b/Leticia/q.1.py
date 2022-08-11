n = 1
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
print("digite 0 para sair ")
while n > 0:
    n = int(input("digite um numero: "))
    if n > 0 and n< 25:
        soma1 = soma1 + 1
    elif n > 26 and n <50:
        soma2 = soma2 + 1
    elif n > 51 and n < 75 :
        soma3 = soma3 + 1
    elif n > 76  and n < 100:
        soma4 = soma4 + 1
print("ha ",soma1,"numeros entre 0 e 25", soma2,"numeros entre 26 e 50",soma3,"numeros entre 51 e 75",soma4,"numeros entre 76 e 100")

#25 pontos