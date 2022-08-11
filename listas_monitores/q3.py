a = 0

c = 0

media = 0

while a < 20:
    b = int(input())

    media = media + b

    if b >= 7:
        c = c + 1
    a = a + 1

print(f"Quantidade de alunos com média maior que 7: {c}")

print(f"Média aritmética da turma {media / 20}")