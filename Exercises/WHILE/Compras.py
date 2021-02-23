print('-' * 29)
print('     Loja Super Baratão')
print('-' * 29)
menor = tot1000 = total = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: R$'))
    cont += 1
    total += preço
    continuação = ' '
    if preço > 1000:
        tot1000 += 1
    while continuação not in 'SN':
        continuação = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuação == 'N':
        break
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome


print('-' * 10 ,end='')
print(' FIM DO PROGRAMA ', end='')
print('-' * 10)
print(f'O total da compra foi de R${total}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor}')