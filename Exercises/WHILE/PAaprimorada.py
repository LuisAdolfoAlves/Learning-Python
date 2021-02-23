p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
termo = p
total = 0
mais = 10
while mais != 0:
      total = total + mais
      while cont <= total:
            print('{}'.format(termo), end='')
            print(' -> ' if cont == 10 else ' -> ', end='')
            cont += 1
            termo += r
      print('Pausa')
      mais = int(input('Quantos termos você que mostrar a mais? '))
print('progressão finalizada com {} termos'.format(cont))
