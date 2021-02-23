s = 1
c = maior = menor = cont = k = 0
while c != 'N':
      s = int(input('Digite um número: '))
      c = str(input('Quer continuar? [S/N] ')).strip().upper()
      cont += 1
      k += s
      if cont == 1:
            maior = menor = s
      else:
            if s > maior:
                  maior = s
            if s < menor:
                  menor = s
media = k / cont
print('Você digitou {} números e a média entre eles é {:.1f}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
