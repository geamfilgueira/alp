num = 0
a = 0
# números de 0 à 25
b = 0
# números de 26 à 50
c = 0
# números de 51 à 75
d = 0
# números de 76 à 100
while num >= 0:
    num = int (input("Insira o número: "))
    if num >= 0 and num <= 25:
        a = a + 1
    elif num >= 26 and num <= 50:
        b = b + 1
    elif num >= 51 and num <= 75:
        c = c + 1
    elif num >= 76 and num <= 100:
        d = d + 1
print ("A quantidade de números entre 0 e 25: ",a)
print ("A quantidade de números entre 26 e 50: ",b)
print ("A quantidade de números entre 51 e 75: ",c)
print ("A quantidade de números entre 76 e 100: ",d)

#25 pontos