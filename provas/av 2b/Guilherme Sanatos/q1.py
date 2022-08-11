i=int(input('digite um numero'))
s=0
d=0
f=0
g=0


while i >=0:

    if i >=51 and i <=75:
        f=f+1
    if i >=76 and i <=100:
        g=g+1
    if i >=26 and i <=50:
        d=d+1
    if i >=0 and i <=25:
        s=s+1
    i=int(input("digite um novo numero"))


#25 pontos
















print('numeros entre 0 e 25: ' ,s)
print('numeros entre 26 e 50: ' ,d)
print('numeros entre 51 e 75: ' ,f)
print('numeros entre 76 e 100: ',g)




