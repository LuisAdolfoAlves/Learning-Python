from random import randint
maior = menor = 0
k = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
     randint(0, 9))
print(f'Os valores sorteados foram: {k}')
print(f'O valor máximo foi: {sorted(k)[-1]}') # ou {max(k)}
print((f'O menor valor foi: {sorted(k)[0]}')) # ou {min(k)}