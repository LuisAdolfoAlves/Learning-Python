print('=' * 30)
print('Jogo: Pedra, Papel e Tesoura')
print('=' * 30)
import random
from time import sleep
print('''
[ 1 ] = Pedra
[ 2 ] = Papel
[ 3 ] = Tesoura''')
escolha = int(input('escolha uma opção: '))
computador = random.randint(1, 3)
sleep(0.25), print('JO')
sleep(0.75), print('KEN')
sleep(1.0), print('PO!!!')
if escolha == computador:
    print('Foram escolhidas as mesmas opções, jogue novamente!')
elif escolha == 1 and computador == 2:
    print('''O computador escolheu PAPEL e você escolheu PEDRA. 
          VOCÊ PERDEU!''')
elif escolha == 1 and computador == 3:
    print('''O computador escolheu TESOURA e você escolheu PEDRA. 
          VOCÊ GANHOU! ''')
elif escolha == 2 and computador == 1:
    print('''O computador escolheu PEDRA e você escolheu PAPEL. 
          VOCÊ GANHOU!''')
elif escolha == 2 and computador == 3:
    print('''O computador escolheu TESOURA e você escolheu PAPEL. 
          VOCÊ PERDEU!''')
elif escolha == 3 and computador == 1:
    print('''O computador escolheu PEDRA e você escolheu TESOURA. 
          VOCÊ PERDEU!''')
elif escolha == 3 and computador == 2:
    print('''O computador escolheu PEDRA e você escolheu TESOURA. 
          VOCÊ GANHOU!''')

'''item = ('Pedra' , 'Papel', 'Tesoura')
computador = randint(0, 2)
print(' o computador escolheu {}'.format(item[computador])
'''