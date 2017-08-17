dicionario = {'Micael':'Python',
              'Luiz':'C#',
              'Rodrigo':'Python',
              'Monica':'Java'}
pessoa = ['Micael']
for nome in dicionario.keys():
    print(nome.title())
    if nome in pessoa:
        print('A linguagem favorita de '+nome.title() +' é '+ dicionario[nome].title())