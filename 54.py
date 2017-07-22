lista = ['Banana','Melão','Morango','Melância']
lista2 = (lista[:])
lista.append('Goiaba')
lista2.append('Abacate')
print('\nFrutas que eu gosto')
for x in lista:
    print(x)
print('\nFrutas que meu amigo gosta')
for c in lista2:
    print(c)