lista = list()
lista_p = list()
lista_i = list()
valor = int(input('Digite um valor: '))
lista.append(valor)
if valor % 2 != 0:
    lista_i.append(valor)
else:
    lista_p.append(valor)
while True:
    continuação = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if continuação in 'N':
        break
    elif continuação in 'S':
        valor = int(input('Digite um valor: '))
        lista.append(valor)
        if valor % 2 != 0:
            lista_i.append(valor)
        else:
            lista_p.append(valor)
    else:
        continuação1 = str(input('Opção inválida. Tente novamente com "SIM" ou "NÃO": ')).strip().upper()[0]
        if continuação1 in 'S':
            valor = int(input('Digite um valor: '))
            lista.append(valor)
            if valor % 2 != 0:
                lista_i.append(valor)
            else:
                lista_p.append(valor)
print('=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_p}')
print(f'A lista de números impares é {lista_i}')
