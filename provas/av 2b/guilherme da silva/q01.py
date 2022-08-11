i=0
ii=0
iii=0
iv=0
n=0
while i >= 0:
    n= int(input("digite um numero: "))
    if n > 0 and n < 25:
         i = i + 1
    elif n >= 26 and n <= 50:
        ii = ii + 1
    elif n >= 51 and n <= 75:
        iii = iii + 1
    elif n >= 76 and n <= 100:
         iv  = iv + 1
    elif n > 100:
        print ('digite numeros menores que 100')
    elif n < 0:
        break

print ("numero negativo inserido. apresentando resultados: ")
print ("numeros entre [0 e 25]", i)
print ("numeros entre [26 e 50]", ii)
print ("numeros entre [51 e 75]", iii)
print ("numeros entre [76 e 100]", iv)



#25 pontos