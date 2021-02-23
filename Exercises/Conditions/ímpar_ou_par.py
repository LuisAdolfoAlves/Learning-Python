import math

a = int(input('Digite um número qualquer: '))
c = a % 2

if c == 1:
    print('O número {} é ímpar'.format(a))
else:
    print('O número {} é par'.format(a))
