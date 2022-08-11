i = 1
soma = 0
d = 2
fat = 0
while i >= 0:
    n = int(input("Digite um numero:"))
    n1 = n - 1
    n = n*n1
    soma = i + d
    fat = fat + i
    while fat <= n:
        e = soma/fat
        print("e =",e)

#errou