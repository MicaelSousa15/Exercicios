lista = []
for lista_numero in range(30):
    nova_lista = {'cor':'verde','pontos':5,'velocidade':'baixa'}
    lista.append(nova_lista)
for list in lista[:5]:
    print(list)
print('Existem ' +str(len(lista))+ ' dicionarios na lista')
#Fiz um loop pra criar 30 dicionarios na lista, e depois imprimi apenas os 5 primeiros