#Calcula o IMC de uma pessoa
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

calculo = peso / ( altura ** 2)

if calculo < 18.5:
    print('O seu IMC "{:.2f}" Você está ABAIXO do peso'.format(calculo))
elif 18.6 < calculo < 24.9:
    print('Parabéns, seu IMC "{:.2f}" indica que você está SAUDAVEL'.format(calculo))
elif 25 < calculo < 29.9:
    print('O IMC "{:.2f}" indica que você tem peso em excesso'.format(calculo))
elif 30 < calculo < 34.9:
    print('O IMC "{:.2f}" indica que você tem Obesidade grau I'.format(calculo))
elif 35 < calculo < 39.9:
    print('O IMC "{:.2f}" indica que você tem obesidade grau II, obesidade severa'.format(calculo))
else:
    print('O IMC "{:.2f}" indica que voce tem obesidade grau III, obesidade mórbida'.format(calculo))
