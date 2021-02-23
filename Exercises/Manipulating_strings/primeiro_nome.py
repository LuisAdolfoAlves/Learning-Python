nome = str(input('Digite o seu nome: ')).strip()

n = nome.split()
print('Seu primeiro nome é: {}{}{}'.format('\033[1;35m', n[0], '\033[m'))
print('Seu ultimo nome é: {}{}{}'.format('\033[1;34m', n[-1], '\033[m'))


# ou p/ ultimo nome ".format(nome[len(nome)-1])
