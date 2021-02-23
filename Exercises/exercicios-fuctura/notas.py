print('Digite as 3 notas do aluno com valores de 0 a 10!')
print('-'*50)
notas = []
for nota in range(1, 4):
    valor = int(input(f'Digite a {nota}ª nota: '))
    while valor > 10 or valor < 0:
        valor = float(input('Valor fora dos limites, Digite novamente: '))
    notas.append(valor)
media = (notas[0] + notas[1] + notas[2]) / 3
print(f'Suas notas foram {notas[0]}, {notas[1]}, {notas[2]} e sua média foi: {media:.2f}.')
if media > 6:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
