#Mostra o numero fatiado em unidade, dezena, centena e milhar
num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}{}{}'.format('\033[1;31m', u, '\033[m'))
print('Dezena: {}{}{}'.format('\033[1:32m', d, '\033[m'))
print('Centena: {}{}{}'.format('\033[1;34m', c, '\033[m'))
print('Milhar: {}{}{}'.format('\033[35m', m, '\033[m'))
