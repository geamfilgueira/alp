#kayque ferreira de albuquerque#
a = int(input("digite seu cpf"))
b = str(input("digite seu nome"))
c = int(input("digite seu tipo de conta"))
vlr = int(input("digite o valor investido"))
mss = int(input("digite a quantidade de meses que investiu"))
g = 0.005 * mss
k = 0.01 * mss
l = 0.015 * mss
if c == 1 :
    print ((vlr*g)+vlr)
elif c == 2 :
    print ((vlr*k)+vlr)
elif c == 3 :
    print ((vlr*l)+vlr)


#ok 
# 20