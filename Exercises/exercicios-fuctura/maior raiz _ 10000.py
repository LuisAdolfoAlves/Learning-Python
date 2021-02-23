from math import sqrt
maior = 0
for numero in range(10000, -1, -1):
    if numero == 9999:
        maior = int(sqrt(numero))
    else:
        if int(sqrt(numero)) < maior:
            break
maior_raiz = maior ** 2
print(f'{maior_raiz}')
