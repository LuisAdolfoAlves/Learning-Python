listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.30,
            'Canetas', 22.30,
            'Livro', 89.90)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for posição in range(len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')
    else:
        print(f'R${listagem[posição]:>7}')
