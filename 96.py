dicionario = {'posição_x':0 ,'posição_y': 25, 'velocidade': 'medio'}
print("Posição_x Original: " + str(dicionario['posição_x']))
if dicionario['velocidade'] == 'baixo':
    incremento = 2
if dicionario['velocidade'] == 'medio':
    incremento = 4
else:
    incremento = 6
dicionario['posição_x'] = dicionario['posição_x'] + incremento
print('Nova posição_x: ' + str(dicionario['posição_x']))
# Criei uma nova variavel chamada incremento, e depois adicionei ela ao dicionario