lista = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
lista2 = lista
lista.append('Nono')
lista2.append('Decimo')
print(lista)
print(lista2)
# Isso acontece porque o append serve para a variavel lista, ou seja
# toda vez que eu botar a variavel lista, ela vai com o append junto
