#aluno: Gabriel Kleber da Silva Batista
a = float(input('digite o valor de um dos lados: '))
y = float(input('digite o valor de um dos lados: '))
z = float(input('digite o valor de um dos lados: '))
if a+y < z or a+z < y or z+y < a:
    print('forma um...')
    if a == y == z:
        print('triangulo equilatero')
    elif a == y != z or a != y == z or a == z != y:
        print('triangulo isosceles')
    elif a!=y and y!=z and a != z:
        print('triangulo escaleno')
else:
    print('nao forma um triangulo')
#ok