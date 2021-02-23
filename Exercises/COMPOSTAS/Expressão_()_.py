expressão = str(input('Digite a expressão: '))
v = expressão.count('(')
i = expressão.count(')')
if v != i:
    print('Expressão inválida')
else:
    print('Expressão válida')

#Resolução utilizando listas.

expressão = str(input('Digite a expressão: '))
lista = []
for simb in expressão:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Expressão inválida!')
