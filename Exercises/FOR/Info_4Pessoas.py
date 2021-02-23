somatorio = 0
maior = 0
menos20 = 0
nomevelho = ''
for pessoas in range(1, 5):
    print('======={}ª pessoa======='.format(pessoas))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    somatorio += idade
    media = somatorio / 4  #media das idades
    if sexo == 'F':        #mulheres do sexo feminino
        if idade < 20:     #mulheres com menos de 20 anos
            menos20 += 1
    if pessoas == 1:       #associa a maior idade ao 1˚ valor
        maior = idade
        nomevelho = nome
    else:
        if idade > maior and sexo == 'M':  #pessoa mais velha do sexo masculino
            maior = idade
            nomevelho = nome
print('A média de idade do grupo é {:.1f}'.format(media))
print('O homem mais velho é {} e sua idade é de {} anos'.format(nomevelho, maior))
if menos20 != 0:
    print('{} mulheres têm menos de 20 anos'.format(menos20))
else:
    print('Nenhuma mulher tem menos de 20 anos ou não foram registradas mulheres')