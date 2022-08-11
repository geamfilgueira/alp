e = 0
m = 1
while True:
    n = int(input('Digite um número inteiro e positivo: '))
    if n <= 0:
        print('número invalido')
    else:
        while n > 0:
            m *= n
            n -= 1
        e = 1 + (2/1) + (3/(2 * 1)) + (4/(3 * 2 * 1) + (n/m))
        if n == 0:
            break

print('O valor de e é de {:.1f}'.format(e))