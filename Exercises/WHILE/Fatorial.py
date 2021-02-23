#Calcular o fatorial de um número
num = int(input('Digite um número para calcular seu fatorial: '))
f = num
cont = 1
while f > 0:
    print('{}'.format(f), end=' ')
    print(' x ' if f > 1 else ' = ', end='')
    cont *= f
    f -= 1
print('{}'.format(cont))
