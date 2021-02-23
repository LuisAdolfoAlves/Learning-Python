from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} {}é bissexto{}.'.format(ano, '\033[4;36m', '\033[m'))
else:
    print('O ano de {} {}não é bissexto{}.'.format(ano, '\033[4;31m', '\033[m'))



