pedido = ['Queijo','Pimenta','Catupri','Mostarda','Calabresa','Tomate']
ingredientes = ['Queijo','Calabresa','Tomate']
for x in pedido:
    if x in ingredientes:
        print('Adicionando '+x+'.')
    else:
        print('Desculpe não temos esse ingrediente')