tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite outro número: ')), int(input('Digite o quarto número: ')))
print(f'Você digitou os números {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3)+1}')
else:
        print('Valor 3 não foi digitado')
print(f'Números pares digitados: ', end='')
for n in tupla:
        if n % 2 == 0:
                print(n, end=' ')
