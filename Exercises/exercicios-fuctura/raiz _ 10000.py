from math import sqrt
maior = 0
for numero in range(0, 10000):
    if int(sqrt(numero)) == 0:
        maior = numero
    else:
        if int(sqrt(numero)) > maior:
            maior = sqrt(numero)
maior_raiz = maior ** 2
print(f'{maior_raiz}')
