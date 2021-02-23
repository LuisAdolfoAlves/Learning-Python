from time import sleep
from random import randint
from operator import itemgetter
resultados = dict()
ranking = []
print('Este programa simula o resultado de 4 dados.')
print('Do jogador 1 ao 4.')
print('-'*60)
random = randint(1, 6)
a = resultados['Jogador 1'] = randint(1, 6)
b = resultados['Jogador 2'] = randint(1, 6)
c = resultados['jogador 3'] = randint(1, 6)
d = resultados['jogador 4'] = randint(1, 6)
for k, v in resultados.items():
    print(f'O {k} tirou {v} no dado.')
print('-'*30)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')