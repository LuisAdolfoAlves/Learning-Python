('-=-' * 20)
print('ANALISADOR DE TRIANGULOS')
('-=-' * 20)

p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))

triangulo1 = p < s + t
triangulo1 = p > s - t or p > t - s


if triangulo1 == true:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')



