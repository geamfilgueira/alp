tipo1 = 0
tipo2 = 0
tipo3 = 0
tipo4 = 0

while True:
    num = float(input('Digite um número, números negativos acabam o programa: '))
    if num < 0:
        break
    elif num >= 0:
        if 0 <= num <= 25:
            tipo1 += 1
        elif 26 <= num <= 50:
            tipo2 += 1
        elif 51 <= num <= 75:
            tipo3 += 1
        elif 76 <= num <= 100:
            tipo4 += 1

print('Tem, ao todo, {} no intervalo de 0-25'.format(tipo1))
print('Tem, ao todo, {} no intervalo de 26-50'.format(tipo2))
print('Tem, ao todo, {} no intervalo de 51-75'.format(tipo3))
print('Tem, ao todo, {} no intervalo de 76-100'.format(tipo4))
