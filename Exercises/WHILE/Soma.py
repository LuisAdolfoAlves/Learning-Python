s = 1
cont = k = 0
s = int(input('Digite um número. [0 para parar]: '))
while s != 0:
      cont += 1
      k += s
      s = int(input('Digite um número. [0 para parar]: '))
print('Você digitou {} números e a soma deles foi {}'.format(cont, k))
