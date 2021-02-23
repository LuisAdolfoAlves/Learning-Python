#Calcula ano do alistamento
from datetime import date
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
ano_de_alistamento = ano + 18
k = ano_atual - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))

if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}!'.format(ano_de_alistamento))
elif idade == 18:
    print('Este é o seu ano de alistamento, aliste-se DE IMEDIATO')
elif idade > 18:
    print('O seu ano de alistamento foi há {} anos'.format(idade - 18))
    print('Seu ano de alistamento foi em {}'.format(ano_de_alistamento))
