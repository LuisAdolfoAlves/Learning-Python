from random import randint
from time import sleep
computador = randint(1, 5) #Faz o computador "PENSAR"

cores = {'roxo': '\033[4;35m',
         'azul': '\033[4;34m',
         'verde': '\033[7;32;40m',
         'vermelho': '\033[7;31;40m',
         'fechamento': '\033[m'}

print('-=-' * 18)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-' * 18)

jogador = int(input('Em que número eu pensei?: ')) #Número que o jogador pensou

print('PROCESSANDO...')
sleep(1.5)

if jogador == computador:
    print('{}Parabéns!{} Você acertou!'.format(cores['verde'], cores['fechamento']))

else:
    print('{}Você perdeu!{} eu pensei no número {}{}{} e não no {}{}{}!'.format(cores['vermelho'], cores['fechamento'], cores['roxo'], computador,cores['fechamento'], cores['azul'], jogador, cores['fechamento']))
