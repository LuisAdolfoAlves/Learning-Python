#Identifica se determinada pessoa tem 'Silva' no nome
name = input('Digite o nome completo: ')

v1 = name.title()
v1 = 'Silva' in v1

if v1 == True:
    print("Seu nome tem 'Silva'? {}{}{}".format('\033[4;32m', v1, '\033[m'))
else:
    print("Seu nome tem 'Silva'? {}{}{}".format('\033[4;31m', v1, '\033[m'))

