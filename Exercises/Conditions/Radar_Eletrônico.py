velocidade = float(input('Digite a velocidade do carro no momento da medição: '))       #Pede a velocidade do carro

cálculo = velocidade - 80     #Verifica se a velocidade do carro foi excedente
multa = cálculo * 7     #Caso tenha sido excedente, calcula o valor da multa

if velocidade > 80:
    print('Você excedeu o limite permitido (80 Km/h), \nportanto deverá pagar uma multa de R${:.2f}:\n '.format(multa))
else:
    print('O carro estava dentro dos limites estabelecidos.')
