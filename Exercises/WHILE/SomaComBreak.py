soma = cont = 0
while True:
      numero = int(input('Digite um número: '))
      if numero == 999:
            break
      cont += 1
      soma += numero
print(f'você digitou {cont} números que somados valem {soma}')
