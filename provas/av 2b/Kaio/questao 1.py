n = int(input("digite um numero positivo:"))
int1 = 0
int2 = 0
int3 = 0
int4 = 0

while n >= 0:
    n = int(input("digite um numero positivo:"))
    if n > 0 and 25 < n:
            int1 = int1 + 1
    elif n > 26 and 50 < n:
            int2 = int2 + 1
    elif n > 51 and 75 < n:
            int3 = int3 + 1
    elif n > 76 and 100 < n:
            int4 = int4 + 1

print("intervalo 1 eh: n > 0 and 25 < n ",int1, "intervalo 2 eh: n > 26 and 50 < n", int2,"intervalo 3 eh: n > 51 and 75 < n", int3,"intervalo 4 eh: n > 76 and 100 < n", int4)


#25 pontos