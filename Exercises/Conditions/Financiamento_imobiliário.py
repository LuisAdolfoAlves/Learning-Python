from time import sleep
print('-=-' * 13)
print('Simulador De Financiamento Imobiliário')
print('-=-' * 13)

nome = str(input('Qual o seu nome? ')).strip()     #Pergunta o nome do cliente
print('Vou te ajudar a ter sua casa própria, {}{}{}!'.format('\033[32m', nome, '\033[m'))

print('{}Primeiro{}, gostaria de saber qual o valor da casa em questão! '.format('\033[4;32m', '\033[m'))
preço = float(input('Digite o {}valor da casa:{}R$ '.format('\033[4;36m', '\033[m'))) #Pergunta o valor da casa ao cliente

print('Agora gostaria de saber o seu salário e em quantos anos pretende pagar a casa:')
salário = float(input('Digite o {}seu salário:{}R$ '.format('\033[4;36m', '\033[m')))   #Pergunta o salário
tempo = int(input('Tempo em que pretende pagar a casa, {}em anos:{} '.format('\033[4;36m', '\033[m')))  #Pergunta o tempo de pagamento

print('OK... {}estou avaliando sua situação...{}'.format('\033[4;33m', '\033[m'))
sleep(1.5)

t = tempo * 12 #transforma anos em meses
prestação = preço / t

if prestação > 30 / 100 * salário:
    print('Para pagar uma casa de {} em {} anos, a prestação será de R${:.2f}.'.format(preço, tempo, prestação))
    print('{}Você não teve o crédito aprovado!{}'.format('\033[4;31m', '\033[m'))

else:
    print('{}Parabéns!{} Você teve o crédito aprovado e está a um passo da casa própria! \nSua prestação mensal será de R${}{:.2f}{} \n'.format('\033[4;32m', '\033[m', '\033[32m', prestação, '\033[m'))
