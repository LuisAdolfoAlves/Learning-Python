from time import sleep


def main():

    print()
    print('Contagem de um a dez com passo 1:')
    lines()
    counting_1()
    lines()

    print()

    print('Contagem de 10 a 0 com de 2 em 2:')
    lines()
    counting_2()
    lines()

    print()

    print('Agora é sua vez de personalizar a contagem! ')
    lines()
    personalize()
    lines()


def counting_1():
    for i in range(1, 11):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


def counting_2():
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


def personalize():
    start = int(input('Início: '))
    end = int(input('Fim: '))
    step = int(input('passo: '))
    print(f'Contagem de {start} até {end} com passo de {step}')
    for i in range(start, end, step):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


def lines():
    print('-' * 40)


if __name__ == '__main__':
    main()
