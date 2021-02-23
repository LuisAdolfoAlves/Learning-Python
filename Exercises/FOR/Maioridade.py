from datetime import date
ano_atual = date.today().year
contmaior = 0
contmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(pessoa)))
    idade = ano_atual - nascimento
    if idade <= 18:
        contmenor += 1
    else:
        contmaior += 1
print('Temos {} pessoas menores de idade'.format(contmenor))
print('e também temos {} pessoas maiores de idade'.format(contmaior))
