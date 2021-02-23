num = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão desejada para esta P.A.: '))

for pa in range(1, 11):
    pa = num + (pa - 1) * razao
    print(pa, end=' ')
