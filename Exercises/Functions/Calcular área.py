print(f'Controle De Terreno')
print('-='*10)


def area(larg, comp):
    a = larg * comp
    print(f' A área de um terreno {larg} x {comp} é de {a} m')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
