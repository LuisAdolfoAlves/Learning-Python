s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('O somatório dos {} números pares informados é {}'.format(cont, s))
