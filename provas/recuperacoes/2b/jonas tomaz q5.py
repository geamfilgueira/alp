cont_aluno = 0
menor_idade = 500
alun_aptidao = 0
aluno_comput = 0
cont_adm  = 0
cont_com = 0
cont_med = 0
cont_dir = 0
cont_jon = 0
aluno_adm = 0
aluno_c = 0
aluno_m = 0
aluno_d = 0
aluno_j = 0
while True:
    nome = input("digite seu nome: ")
    curso = input("diga qual seu curso administracao, computacao, medicina, direito e jornalismo: ")
    mot_escolha = input("qual o motivo de sua escolha remuneracao, aptidao ou outros: ")
    idade = int(input("digite sua idade: "))
    genero = input("digite seu genero m/f: ")
    sair = input("digite fim se quiser sair: ")
    cont_aluno += 1
    if curso == "adiminidtracao":
        aluno_adm +=1
    if curso == "computacao":
        aluno_c +=1
    if curso == "medicina":
        aluno_m +=1
    if curso == "direito":
        aluno_d +=1
    if curso == "jornalismo":
        aluno_j +=1

    if idade < 20 and mot_escolha == "aptidao":
        alun_aptidao += 1
    elif menor_idade < idade and mot_escolha == "remuneracao":
        menor_idade = idade
        print(idade)
        print(nome)
    elif idade == idade and mot_escolha == "computacao":
        aluno_comput += 1
        media_comput = idade / aluno_comput
    if genero == "f" and curso == "adiministracao":
        cont_adm += 1
    elif genero == "f" and curso == "computacao":
        cont_com += 1
    elif genero == "f" and curso == "medicina":
        cont_med += 1
    elif genero == "f" and curso == "direito":
        cont_dir += 1
    elif genero == "f" and curso == "jornalismo":
        cont_jon += 1
    if sair == "fim":
        break
print(media_comput)
print("percentual em adimistracao e, ", aluno_adm / cont_aluno)
print("percentual em direito e, ", aluno_d / cont_aluno)
print("percentual em medicina e, ", aluno_m / cont_aluno)
print("percentual em computacao e, ", aluno_c / cont_aluno)
print("percentual em jornalismo e, ", aluno_j / cont_aluno)
#ok