numero = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'seis', 'sete', 'oito',\
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',\
'dezoito', 'dezenove', 'vinte')
opção = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
while True:
    if opção > 20:
        opção = int(input('Por favor digite um número válido:  '))
    elif opção < 0:
        opção = int(input('Por favor digite um número válido:  '))
    if opção <= 20:
        print(f'O número escolhido foi {opção} e por extenso é {numero[opção]}')
        if True:
            continuação = str(input('Quer continuar? [S/N]')).strip().upper()
            if continuação in 'S':
                opção = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
            else:
                break
print('Programa encerrado!')
