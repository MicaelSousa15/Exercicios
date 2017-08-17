lista = []
for lista_numero in range(30):
    nova_lista = {'cor':'verde','pontos':5,'velocidade':'baixa'}
    lista.append(nova_lista)
for list in lista[0:3]:
    if list['cor'] == 'verde':
        list['cor'] = 'amarelo'
        list['velocidade'] = 'media'
        list['pontos'] = 25
for list in lista[0:5]:
    print(list)
# Fiz um loop pra criar 30 dicionarios na lista, e depois modifiquei os 3 primeiros
# e imprimi os 5 primeiros