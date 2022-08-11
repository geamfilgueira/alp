N1 = int(input("Digite um número"))

I1 = 0
I2 = 0
I3 = 0
I4 = 0

while N1 >= -1:
    if N1 >= 0 and N1 <= 25:
         I1 = I1 + 1
    elif N1 >= 26 and N1 <= 50:
         I2 = I2 + 1
    elif N1 >= 51 and N1 <= 75:
         I3 = I3 + 1
    elif 76 <= N1 <= 100:
         I4 = I4 + 1

print("A quantidade de números do Intervalo 1 é", I1)
print("A quantidade de números do Intervalo 2 é", I2)
print("A quantidade de números do Intervalo 3 é", I3)
print("A quantidade de números do Intervalo 4 é", I4)

#considerei 12 pontos