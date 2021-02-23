cont = 0
num = int(input('Digite um número: '))

for x in range(1, num + 1):
    if num % x == 0:
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(x, end='')
    c = num % x #Acha o resto da divisão
    if c == 0:
        cont += 1
print('\033[m \nO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('Portanto, o número \033[32m{} É PRIMO'.format(num))
else:
    print('Portanto, o número \033[31m{} NÃO É PRIMO'.format(num))
