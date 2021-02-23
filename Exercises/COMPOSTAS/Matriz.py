matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"Digite na posição [{linha+1}, {coluna+1}] na lista: ")))
print('-='*30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}:^5]', end='')
    print()
