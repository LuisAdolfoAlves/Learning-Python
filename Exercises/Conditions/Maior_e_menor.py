p = float(input('Digite o primeiro valor:'))
s = float(input('Digite o segundo valor:'))
t = float(input('Digite o terceiro valor:'))

cores = {'amarelo': '\033[30;43m',
        'vermelho': '\033[30;41m',
        'fechamento': '\033[m'}

#verificando quem é maior

if p > s > t:
    print('O maior número é {}{}{}'.format(cores['amarelo'], p, cores['fechamento']))
elif s > t: print('O maior número é {}{}{}'.format(cores['amarelo'], s, cores['fechamento']))
else:
    print('O maior número é {}{}{}'.format(cores['amarelo'], t, cores['fechamento']))

#verificando quem é menor

if p < s < t:
    print('O menor número é {}{}{}'.format(cores['vermelho'], p, cores['fechamento']))
elif s < t:
    print('O menor número é {}{}{}'.format(cores['vermelho'], s, cores['fechamento']))
else:
    print('O menor número é {}{}{}'.format(cores['vermelho'], t, cores['fechamento']))

# OU
''' menor = a
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c
    
#verificando o maior
     maior = a 
if b > a and b > c:
     maior = b
if c > a and c > b:
    maior = c '''
