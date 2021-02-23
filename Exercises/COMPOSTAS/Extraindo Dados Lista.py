lista = []
valor = lista.append(int(input('Digite um valor: ')))
while True:
    continuação = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if continuação in 'N':
        break
    elif continuação in 'S':
        valor = lista.append(int(input('Digite um valor: ')))
    else:
        continuação1 = str(input('Opção inválida. Tente novamente com "SIM" ou "NÃO": ')).strip().upper()[0]
        if continuação1 in 'S':
            valor = lista.append(int(input('Digite um valor: ')))
print('=' * 30)
print(f'Você digitou {len(valor)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor "5" faz parte da lista!')
else:
    print(f'O valor "5" não faz parte da lista!')
