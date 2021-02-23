from random import randint
print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 12)
print('Use valores de 0 a 10 para este jogo.')
print('Ganhe quantas vezes for capaz! Boa sorte!!')
contador = 0
while True:
     jogador = int(input('Diga um valor: '))
     opção = str(input('Ímpar ou Par? [P/I]')).strip().upper()[0]
     computador = randint(0, 10)
     s = computador + jogador
     k = s % 2
     if k == 0:
         print('-' * 62)
         print(f'você jogou {jogador} e o computador jogou {computador}. Totalizando {s}, Deu Par.')
     else:
         print('-' * 62)
         print(f'você jogou {jogador} e o computador jogou {computador}. Totalizando {s}, Deu Ímpar.')
     print('-' * 62)
     if opção == 'P' and k != 0:
         break
     else:
         print('-' * 12)
         print('Você Ganhou!')
         print('-' * 12)
         contador += 1
print('Você perdeu!')
print('-' * 30)
print(f'GAME OVER! você venceu {contador} vezes')
print('=-' * 15)