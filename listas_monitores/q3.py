cont    = 0
nota    = 0
cont_aluno = 0
media = 0
while nota >=0:
    nota = float(input("Digite a nota do aluno ou nota negativa para sair: "))
    if nota >= 0:
        media = media + nota
        cont_aluno+=1
        if nota >= 7:
            cont=cont+1
print ("Alunos com nota >= 7 ", cont)
print("A media de notas da turma eh: ", media/cont_aluno)