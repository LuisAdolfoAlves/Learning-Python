valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(f'Sua lista foi {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for posição, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posição+1}..', end='')
print()
print(f'O menor valor digitado foi {min(valores)} na posição ', end='')
for posição, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posição+1}..', end='')
