from random import randint
print('-----------Jogo da adivinhação-----------')
print('Olá, sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
cont = 0
p = int(input('Seu palpite: '))
n = randint(0, 10)
'''Acertou = False
   while not acertou:'''
while p != n:
    cont += 1
    if p > n:
        print('Menos... tente mais uma vez.')
        p = int(input('Seu palpite: '))
    else:
        print('Mais... Tente mais uma vez.')
        p = int(input('Seu palpite: '))
print('Parabéns! Você acertou com {} tentativas'.format(cont))