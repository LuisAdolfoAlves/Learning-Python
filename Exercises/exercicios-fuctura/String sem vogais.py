#Lê uma string e diz quantas consoantes tem na string
string = str(input('Digite uma string: '))
nova_string = string
vogais = ('a', 'e', 'i', 'o', 'u')

for letras in string.lower():
        if letras in vogais and letras.isalpha():
             nova_string = nova_string.replace(letras, "")
print(f'A string "{string}" sem vogais possui "{len(nova_string)}" consoantes que são: {nova_string}')
