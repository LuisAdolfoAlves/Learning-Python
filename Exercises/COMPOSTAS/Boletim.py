ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continua = str(input('Quer continuar? [S/N]'))
    if continua in 'nNñ':
        break
print('-='*15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f' Notas de {ficha[opc][0]}: {ficha[opc][1]}')
print('Programa encerrado')
