p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
termo = p
while cont <= 10:
      print('{}'.format(termo), end='')
      print(' = ' if cont == 10 else ' -> ', end='')
      cont += 1
      termo += r
print('FIM')