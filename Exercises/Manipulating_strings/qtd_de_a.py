#Identifica a quantidade de 'a' numa frase
fr = input('Digite uma frase: ').strip().lower()



x = fr.count('a')
y = fr.find('a')+1
z = fr.rfind('a')+1

print('A quantidade de "a" é {}{}{}'.format('\033[4;35m', x, '\033[m'))
print('A posição do primeiro "a" é {}{}{}'.format('\033[4;36m', y, '\033[m'))
print('A posição do último "a" é {}{}{}'.format('\033[4;31m', z, '\033[m'))
