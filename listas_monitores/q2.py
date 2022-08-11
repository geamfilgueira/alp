a = int(input("Digite um numero: "))
b = 0 # inicializando com 0 para representar o primeiro par (quanto num positivo) ou o último par ( quando o num for negativo)

if a > 0:
    while b < a:
        print("Par positivo: ", b)
        b = b + 2
else:
    while a <= b:
        if a % 2 == 0:
            print("Par negativo: ", a)
        a = a + 1