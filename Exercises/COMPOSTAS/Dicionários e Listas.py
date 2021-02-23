dados = dict()
pessoal = list()
idade = list()
mulheres = list()
acima_media = dict()


def coleta_de_dados():
    dados.clear()
    dados['nome'] = str(input('Nome: ')).capitalize()
    dados['idade'] = int(input('Idade: '))
    idade.append(dados['idade'])
    sexo()
    pessoal.append(dados.copy())


def sexo():
    while True:
        sexo = str(input('Sexo: ')).upper().strip()[0]
        if sexo in 'F':
            mulheres.append(dados['nome'])
        if sexo in 'MF':
            dados['sexo'] = sexo
            break
        print('ERRO! Use apenas M ou F')


while True:
    coleta_de_dados()
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()
        if continua in 'SN':
            break
        print('ERRO! Use apenas S ou N.')
    if continua in 'N':
        break

media = sum(idade) / len(pessoal)

def idade_acima_media():
    print(f'D) Lista de pessoas com idade acima  da média:')
    for i in pessoal:
        if i['idade'] >= media:
            print('    ', end='')
            for k, v in i.items():
                print(f'--> {k} = {v}', end=' ')
            print()


print('-='*20)
print(f'A) Ao todo temos {len(pessoal)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.1f} anos')
print(f'C) As mulheres cadastradas foram:  ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print()
idade_acima_media()
print('<<PROGRAMA ENCERRADO>> ')

