from time import sleep
p = int(input('Digite o primeiro valor: '))
s = int(input('Digite o segundo valor: '))
n = 0
maior = 0
while n != 5:
    sleep(1.5)
    print('=-=' * 10)
    print('escolha uma das opções abaixo: ')
    print('''
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    n = int(input('Qual a sua opção? '))
    
    if n == 1:
        print('A soma entre {} + {} é {}'.format(p, s, p + s))
   
    if n == 2:
        print('A multiplicação entre {} x {} é {}'.format(p, s, p * s))
    
    if n == 3:
        
        if p > s:
            print('O maior número é {}'.format(p))
        
        else:
            print('O maior número é {}'.format(s))
    
    if n == 4:
        p = int(input('Digite o primeiro valor: '))
        s = int(input('Digite o segundo valor: '))
    
    if n == 5:
        print('Finalizando...')
        sleep(1)
    
    else:
        print('Opção inválida. Tente novamente!')
        
print('=-=' * 10)
print('Fim do programa!')


