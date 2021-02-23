km = float(input('Qual a distância da sua viagem em km?'))
print('Você está prestes a embarcar numa viagem de {} km'.format(km))

#ou
# preço = km * 0.5 if km <= 200 else km * 0.45
if km <= 200:
    c1 = km * 0.5
    print('O preço da sua passagem será de R${:.2f}. Boa viagem!!'.format(c1))
else:
    c2 = km * 0.45
    print('O preço da sua passagem será de R${:.2f}. Boa viagem!!'.format(c2))
