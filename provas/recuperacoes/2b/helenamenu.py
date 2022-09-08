while True:
    print("---------MENU--------\n"
        "| <1> questao 1        |\n"
        "| <2> questao 2        |\n"
        "| <3> questao 3        |\n"
        "| <4> questao 4        |\n"
        "| <5> questao 5        |\n"
        "| <0> para sair        |\n"
         "-----------------------")
    op = int(input("digite_uma_opcao: "))

    if op == 0:
        break

    elif op == 1:
        pre = 0
        quant_mes = 0

        codico = 0
        resid = []
        comer = []
        ind = []

        cons_verif = 0

        media = 0
        total = 0
        soma = 0

        maior = -100
        menor = 1000


        while True:
            numero = int(input("digite o numero do consumidor:  "))
            if numero == 0:
                break
            else:

                pre = float(input("digite o preco do kmh consumido: "))
                quant_mes = float(input("digite a quantidade de kmh consumidos durante o mes: "))
                codico = int(input("digite 1- residencial, 2- comercial, 3-indistrial; "))

                cons_verif = (quant_mes * pre)

                if cons_verif >= maior:
                    maior = cons_verif

                elif cons_verif <= menor:
                    menor = cons_verif

                total += 1
                soma += cons_verif

                if codico == 1:
                    resid.append(quant_mes)

                elif codico == 2:
                    comer.append(quant_mes)

                elif codico == 3:
                    ind.append(quant_mes)

#solução com a logica errada: 15
        #1
        print ("MAIOR CONSUMO VERIFICADO = ", maior)
        print ("MENOR CONSUMO VERIFICADO = ", menor)

        #2
        media = total/cons_verif
        print("MEDIA GERAL DO CONSUMO = ", media)

        #3
        print ("TOTAL RESIDENCIAL = ", resid)
        print ("TOTAL COMERCIAL = ", comer)
        print ("TOTAL INDUSTRIAL = ", ind)

    elif op == 2:
        print ("QUESTAO 02")
        n = int(input("digite um numero inteiro: "))

        X = 1
        i = 2
        if n > 0:
            while i <= n:
                X = X + ((i/(i - 1)**1))
                i += 1

        else:
            print("numero invalido")

        print ("O VALOR DE X = ",X )
#ok
    elif op == 3:
        print("QUESTAO 03")
        x = int(input("digite um numero: "))
        lista = []

        while True:
            num = int(input("digite os numeros: "))

            if (num + num) == (x**3):
                lista.append(num)
                break

            else:
                lista.append(num)

        print("TOTAL DE NUMEROS DITOS PELO USUARIO = ", lista)
#Errada
    elif op == 4:
        print ("QUESTAO 04")
        div_exat = 0
        div_n = 0

        i = 1
        n = int(input("digite um numero qualquer: "))

        while i <= n:
            i += 1

            if n%i == 0:
                div_exat += 1

            elif n%i == 1:
                div_n += 1

        print ("QUANTIDADE DE DIVISORES EXATOS = ",div_exat)
        print ("QUANTIDADE DE DIVISORES NAO EXATOS = ", div_n)
        print ("O NUMERO ESCOLHID0 = ", n)
#vc precisa ler melhor o que se pede na questao: ok
    elif op == 5:
        print("QUESTAO 5")
        curso = 0
        motivo = 0
        idade = 0
        genero = 0
        fem = 0
        mas = 0
        sair = " "

        total = 0

        adm = 0
        perc_adm = 0
        comput = 0
        media_idade_comp = 0
        soma1 = 0
        total_idade = 0

        perc_comp = 0
        med = 0
        perc_med = 0
        diret = 0
        perc_diret = 0
        jorn = 0
        perc_jorn = 0

        idade_20_apt = 0
        ren_prof = 0
        ren_apd = 0
        outro = 0

        curso_freg_fem_adm = 0
        curso_freg_fem_comp = 0
        curso_freg_fem_medic = 0
        curso_freg_fem_diret = 0
        curso_freg_fem_jorn = 0


        while sair != 1:
            curso = int(input('''digite seu curso:
        1 - ADMISTRACAO\n
        2 - COMPUTACAO\n
        3 - MEDICINA\n
        4 - DIREITO\n
        5 - JORNALISMO\n '''))

            motivo = int(input('''qual o motivo da escolha?:
        1 - RENUMERACAO OBTIDA PELA PROFISSAO\n
        2 - APTIDAO\n
        3 - OUTRA\n '''))

            idade = int(input("digite a idade: "))
            genero = input("digite seu genero: 1- fem, 2- mas ")
            total += 1


            if genero == 1:
                if curso == 1:
                    curso_freg_fem_adm += 1
                    if curso == 2:
                        curso_freg_fem_comp += 1
                        if curso == 3:
                            curso_freg_fem_medic += 1
                            if curso == 4:
                                curso_freg_fem_diret += 1
                                if curso == 5:
                                    curso_freg_fem_comp += 1
            else:
                continue


            if motivo == 2:
                if idade >= 20:
                    idade_20_apt += 1


            if curso == 1:
                perc_adm += 1

            elif curso == 2:
                 perc_comp += 1
                 total_idade += 1
                 soma1 += idade

            elif curso == 3:
                perc_med += 1

            elif curso == 4:
                perc_diret += 1

            elif curso == 5:
                perc_jorn += 1

            sair = int(input("digite sair? 1 - sim ou 2 - nao"))
        #1
        print ("ALUNOS COM IDADE INFERIOR A 20 ANOS ESCOLHEU POR APTIDAO = ", idade_20_apt)

        #2
        print ("PERCENTUAL DE ALUNOS NO CURSO ADMISTRACAO = ", (perc_adm/total) *100)
        print ("PERCENTUAL DE ALUNOS NO CURSO COMPUTACAO = ", (perc_comp/total) *100)
        print ("PERCENTUAL DE ALUNOS NO CURSO MEDICINA = ",(perc_med/total) *100)
        print ("PERCENTUAL DE ALUNOS NO CURSO DIREITO = ", (perc_diret/total) *100)
        print ("PERCENTUAL DE ALUNOS NO CURSO JORNALISMO = ", (perc_jorn/total)*100)

        #3
        media_idade_comp = soma1/idade
        print ("MEDIA DAS IDADES DOS ALUNOS NA COMPUTACAO = ", media_idade_comp)

        #4
        print ("CURSO MAIS FREQUENTADO PELO GENERO FEMININO = ")
        print ("1 - ADMISTRACAO =",curso_freg_fem_adm)
        print ("2 - COMPUTACAO =",curso_freg_fem_comp)
        print ("3 - MEDICINA =",curso_freg_fem_medic)
        print ("4 - DIREITO =", curso_freg_fem_diret)
        print ("1 - ADMISTRACAO =",curso_freg_fem_jorn)

    else:
        print ("opcao invalida!")
#Considerei ok