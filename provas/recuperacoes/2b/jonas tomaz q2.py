n = int(input("digite um numero positivo: "))
x = 0
if x < n:
    while n > 0:
        expo = n
        a = 1
        b = 1
        while expo >= 0:
            calculo = a +(n**b)
            a += 1
            b += 1
            expo = expo - 1
    x = calculo
print(x)

# solucao errada: 


