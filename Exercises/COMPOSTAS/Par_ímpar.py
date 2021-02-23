numeros = [[], []]
p = 0
for n in range(1, 8):
    p = int(input(f'Digite o {n}º valor: '))
    if p % 2 == 0:
        numeros[0].append(p)
    else:
        numeros[1].append(p)
print('-='*30)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram {sorted(numeros[1])}')
