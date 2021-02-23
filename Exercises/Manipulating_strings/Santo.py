#Identifica se o primeiro nome de uma cidade é 'Santo'
nome = str(input('Digite o nome da cidade: ')).strip().lower()

v = nome.split()
v1 = 'santo' in v[0]

if v1 == True:
    print('{}{}{}'.format('\033[4;32m', v1, '\033[m'))
else:
    print('{}{}{}'.format('\033[4;31m', v1, '\033[m'))
