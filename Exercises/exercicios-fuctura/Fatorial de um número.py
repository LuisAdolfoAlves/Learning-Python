'''12 - Escreva uma função que retorne o fatorial de um número.'''

def fatorial_deum_numero():
    import math as m
    numero = int(input('Digite um número: '))
    f = numero
    print('-='*40)
    print(f'Fatorial de {numero}!')
    while f != 0:
        print(f'{f}', end=' ')
        print('x' if f > 1 else '=', end=' ')
        f -= 1
    print(m.factorial(numero))
fatorial_deum_numero()