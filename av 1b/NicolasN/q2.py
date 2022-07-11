print ("A tabela de códigos é Cachorro quente = 100, hamburguer = 101, bauru = 103, válido a partir de dois itens")
pedido= input("Códigos dos pedidos, separe com +:")
if pedido=="100+101":
    print("Seu pedido foi de um cachorro quente e um hamburguer, valor: 6,50")
elif pedido=="100+103":
    print("Seu pedido foi de um cachorro quente e um bauru, valor: 8,00")
elif pedido=="100+100":
    print("Seu pedido foi de dois cachorros quente, valor: 6,00")
elif pedido=="101+103":
    print("Seu pedido foi de um hamburguer e um bauru, valor: 8,50")
elif pedido=="101+100":
    print("Seu pedido foi de um hamburguer e um cachorro quente, valor: 6,50")
elif pedido=="101+101":
    print("Seu pedido foi de dois hamburguers, valor: 7,00")
elif pedido=="103+100":
    print ("Seu pedido foi de um bauru e um cachorro quente, valor: 8,00")
elif pedido=="103+101":
    print ("Seu pedido foi de um bauru e um hamburguer, valor: 8,50")
elif pedido=="103+103":
    print ("Seu pedido foi dois bauru, valor: 10,00")
else:
    print ("Algo deu errado, confira se fez tudo certo")

#logica errada
# 3