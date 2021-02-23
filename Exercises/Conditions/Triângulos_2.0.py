print('-=-' * 10)
print('ANALISADOR DE TRIANGULOS')
print('-=-' * 10)

p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))

triangulo = p < s + t and p > s - t and p > t - s


if triangulo == True:
    print('Os segmentos acima {}PODEM{} formar um triângulo '.format('\033[4;32m', '\033[m'), end='')
    if p == s == t:
        print('EQUILÁTERO')
    elif p != s and p != t and s != t:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima {}NAO PODEM{} formar um triangulo'.format('\033[4;31m', '\033[m'))
