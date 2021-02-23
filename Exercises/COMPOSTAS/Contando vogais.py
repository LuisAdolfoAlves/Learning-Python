listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAS', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavras in listagem:
    print(f'\nNa palavra {palavras} temos ', end='')
    for letra in palavras:
        if letra in 'AÁÃEÉÊIÎÍÓOUÚ':
            print(letra.lower(), end=' ')
