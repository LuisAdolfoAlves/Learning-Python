print('-==-' * 6)
print('Sequência de Fibonacci')
print('-==-' * 6)
cont = 3
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while cont <= termos:
      t3 = t1 + t2
      print(' -> {}'.format(t3), end='')
      t1 = t2
      t2 = t3
      cont+= 1
print(' -> FIM')