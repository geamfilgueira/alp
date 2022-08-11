a = 0

c = 0

media = 0

while a < 20:
    b = int(input("Digite a nota do aluno: "))

    media = media + b

    if b >= 7:
        c = c + 1
    a = a + 1

print("Quantidade de alunos com média maior que 7: ", c)

print("Média aritmética da turma ",  (media / 20))