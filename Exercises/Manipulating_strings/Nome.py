number = int(input('number: '))
count = 0
spaces = '.'

for linha in range(number):
    for coluna in range(number - 1):
        print('', end='')
    print(' ' * (number + 1 - linha), '#' * (linha + 1))



