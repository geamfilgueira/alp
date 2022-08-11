a = int(input())

i = 0

soma = 0
multpl = 1

while i < a:
    b = int(input())
    soma = soma + b
    if i == 0:
        multpl = multpl * b
    elif i == a - 1:
        multpl = multpl * b
    i = i + 1

print(f"A soma de todos os números informados é: {soma}")

print(f"O resultado da multiplicação do primeiro pelo último número é: {multpl}")