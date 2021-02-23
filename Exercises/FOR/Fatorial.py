num = int(input('Digite um número para achar o seu fatorial: '))
cont = 1
for f in range(num, 0, -1):
    print(f, end=' ')
    print(' x ' if f > 1 else ' = ', end=' ')
    cont *= f
print('{}'.format(cont))