pedido = int(input("digite 100 para cachorro quente, 101 para hamburguer e 103 para bauru completo "))
pedido2 = int(input("digite 100 para cachorro quente, 101 para hamburguer e 103 para bauru completo "))

bauru = 5.00
hamburguer = 3.50
cachorro = 3.00
if pedido == 101 and pedido2 == 100:
    quant= int(input("digite a quant de hamburguer: "))
    quant2 = int(input("digite a quant de cachorrro quente: "))
    print ((hamburguer*quant) + (cachorro*quant2))
elif pedido == 100 and pedido2 == 101:
    quant= int(input("digite a quant de cachorro quente: "))
    quant2 = int(input("digite a quant de hambueguer: "))
    print ((cachorro*quant + hamburguer*quant2))
elif pedido == 100 and pedido2 == 103:
    quant= int(input("digite a quant de cachorro quente: "))
    quant2 = int(input("digite a quant de bauru: "))
    print ((cachorro*quant) + (bauru*quant2))
elif pedido == 103 and pedido2 == 100:
    quant= int(input("digite a quant de bauru: "))
    quant2 = int(input("digite a quant de cachorro quente: "))
    print ((bauru*quant) + (cachorro*quant2))
elif pedido == 103 and pedido2 == 101:
    quant= int(input("digite a quant de bauru: "))
    quant2 = int(input("digite a quant de hamburguer: "))
    print ((bauru*quant) + (hamburguer*quant2))
elif pedido == 101 and pedido2 == 103:
    quant= int(input("digite a quant de hamburguer: "))
    quant2 = int(input("digite a quant de bauru: "))
    print ((hamburguer*quant) + (bauru*quant2))


# SHOW
# 20