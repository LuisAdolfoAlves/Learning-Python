cont = 4
login = 'Pernambuco'
senha = 'AmoPernambuco123'
loginin = str(input('Login: ')).strip().upper()
senhain = str(input('Senha: ')).strip()
if senhain == senha:
    print('Login efetuado com sucesso!')
else:
    while True:
        print(f'Senha incorreta! Tentativas restantes: {cont}')
        novamente = str(input('Tente Novamente: '))
        cont -= 1
        if novamente == senha:
            print('Login efetuado com sucesso! Bem-Vindo')
            break
        if cont == 0:
            if novamente != senha:
                print('Conta bloqueada por excesso de tentativas! ')
                break



