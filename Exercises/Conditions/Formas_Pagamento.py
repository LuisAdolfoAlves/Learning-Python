#FORMAS DE PAGAMENTO
total = float(input('Digite o valor total das compras: '))
formas_pag = print('''[ 1 ] = à vista
[ 2 ] = débito à vista
[ 3 ] = 2x no cartão
[ 4 ] = 3x ou mais''')
pagamento = int(input('Selecione uma das opções de pagamento: '))

a_vista = total - 10/100 * total
duas_x= total / 2


if pagamento == 1:
    print(' O valor total {} à vista será {} com 10% de desconto'.format(total, a_vista))
elif pagamento == 2:
    print('Esta opção de pagamento não possui desconto, portanto o valor total sera {}'.format(total))
elif pagamento == 3:
    print('Esta opção de pagamento não possui desconto, portanto o valor será {} em 2x de {:.2f}'.format(total, duas_x))
elif pagamento == 4:
    dvd = int(input('Digite em quantas vezes deseja divir a compra: '))
    calculo = (total + 10/100 * total)/ dvd
    print('Esta opção possui juros, o valor será dividido em {}x e ficará {:.2f} mensais'.format(dvd, calculo))
if pagamento > 4:
    print('Por favor selecione uma opção válida.')