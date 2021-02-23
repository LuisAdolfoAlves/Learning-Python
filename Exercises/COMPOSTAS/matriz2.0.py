matriz = [[], [], []]
lista_p = []
lista_i = []
for linha in range(3):
    for coluna in range(3):
        num = (int(input(f"Digite na posição [{linha+1}, {coluna+1}] na lista: ")))
        matriz[linha].append(num)
        if num % 2 == 0:
            lista_p.append(num)
        else:
            lista_i.append(num)
print('-='*18)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*18)
cont = 0
soma = 0
for _ in lista_p:
    soma += lista_p[cont]
    cont += 1
print(f'a soma dos números pares é {soma}')
soma = 0
cont = 0
for _ in lista_i:
    soma += lista_i[cont]
    cont += 1
print(f'a soma dos números ímpares é {soma}')
stcol = 0
for linha in range(0, 3):
    stcol += matriz[linha][2]
print(f'A soma dos números da terceira coluna é {stcol}')
scol = maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
