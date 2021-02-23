#Diz a categoria de um nadador em função da idade
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta pertence a categoria MIRIM')
elif 9 < idade <= 14:
    print('O atleta pertence a categoria INFANTIL')
elif 14 < idade <= 16:
    print('O atleta pertence a categoria JUVENIL')
elif 16 < idade <= 19:
    print('O atleta pertende a categoria JUNIOR')
elif idade >= 20:
    print('O atleta pertence a categoria SENIOR')
