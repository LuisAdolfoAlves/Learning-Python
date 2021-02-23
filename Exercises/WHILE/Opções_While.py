contador_se = contador_id = contador_mu = 0
pessoas = ''
while True:
    print('-' * 19)
    print('Cadastre uma pessoa')
    print('-' * 19)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 19)
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if idade >= 18:
        contador_id += 1
    if sexo == 'M':
        contador_se += 1
    if sexo == 'F' and idade < 20:
        contador_mu += 1
    if continuação == 'N':
        break
print(f'O total de pessoas com 18 anos ou mais é: {contador_id}.')
print(f'Ao todo temos {contador_se} homens cadastrados.')
print(f'E temos {contador_mu} mulheres com menos de 20 anos')