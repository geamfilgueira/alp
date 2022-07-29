fim = ''
total_alunos = 0
total_s_m = 0
total_s_f = 0
media_idade = 0
soma_idades = 0

maior_idade = -1
menor_idade = 100

while fim != 'sim':
    nome = input("Digite o nome do aluno: ")
    sexo = input("Qual o sexo do aluno (M ou F): ")
    idade = int(input("Digite a idade do aluno: "))
    soma_idades = soma_idades + idade

    if idade > maior_idade:
        maior_idade = idade
    elif idade < menor_idade:
        menor_idade = idade
    
    total_alunos = total_alunos + 1
    if sexo == 'M':
        total_s_m = total_s_m + 1
    else:
         total_s_f = total_s_f + 1
    fim = input("Deseja sair sim ou nao: ")

print ("A media de idade de alunos eh ", soma_idades/total_alunos)
print ("A quantidade de alunos do sexo M ", total_s_m)
print ("A quantidade de alunos do sexo M ", total_s_f)
print ("A maior idade eh ", maior_idade)
print ("A menor idade eh ", menor_idade)