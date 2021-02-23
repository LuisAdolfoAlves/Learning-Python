'''Este pragrama cadastra um trabalhador e diz com quantos anos ele deve se aposentar'''

# Dicionário onde serão adicionados os dados do trabalhador
# O dicionario está vazio no inicio do programa
dados = dict()

# Pede os dados cadastrais do trabalhador, associa na variavel correspondente e armazena no dicionario
dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = int(input('Ano de Nascimento: '))
dados['carteira de trabalho'] = int(input('Carteira de trabalho: (0 para não tem) '))


'''verifica se o trabalhador tem carteira de trabalho e da a estimativa de acordo com o ano de contratação, 
se o trabalhador nao possuir carteira de trabalho o programa pula esta etapa'''
if dados['carteira de trabalho'] != 0:
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['Ano de contratação'] - dados['Ano de nascimento']+ 45


print('-='*20, end='')
print('-')

# Programa printa os dados cadastrais do trabalhador com a idade que o trabalhador deve se aposentar
for k, v in dados.items():
    print(f'- {k}: {v}')
