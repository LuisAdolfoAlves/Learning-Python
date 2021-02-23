num = int(input('Digite um número para gerar a sua respectiva tabuada: '))

for x in range(0, 10):
    resultado = num * (x + 1)
    print('{} x {} = {}'.format(num, x + 1, resultado))
