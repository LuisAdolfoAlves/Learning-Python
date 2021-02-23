print('-' * 62)
print('''PROGRAMA DE TABUADA.
DIGITE UM VALOR PARA EXIBIR A SUA TABUADA
OU DIGITE UM NÚMERO NEGATIVO PARA ENCERRAR O PROGRAMA.''')
print('-' * 62)
while True:
      numero = int(input('Digite um número: '))
      if numero < 0:
            break
      for cont in range(0, 11):
            tabuada = print(f'{numero} X {cont} = {numero * cont}')
print('Programa Encerrado.')