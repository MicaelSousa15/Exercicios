idade = 12
if idade < 4:
    preço = 0
elif idade < 18:
    preço = 5
elif idade < 65:
    preço = 10
else:
    preço = 5
print('Seu custo de admissão é R$'+str(preço)+'.')
# Ele vai pagar 5, pq idade esta entre 4 e 18