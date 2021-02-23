valor = []
digitado = valor.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso!')
while True:
    continuação = str(input('Quer continuar [S/N]? ')).strip()[0]
    if continuação in 'Nn':
        break
    if continuação not in 'NnSs':
        continuação = str(input('Opção inválida. Por favor tente com "Sim" ou "Não": ')).strip()[0]
        if continuação in 'Nn':
            break
    if continuação in 'Ss':
        digitado1 = int(input('Digite um valor: '))
        if digitado1 in valor:
            print('Valor duplicado! Não irei adicioná-lo à lista.')
        elif digitado1 not in valor:
            valor.append(digitado1)
            print('Valor adicionado com sucesso!')
print(f'Você digitou a lista de números {sorted(valor)}')
print('Programa Encerrado!')