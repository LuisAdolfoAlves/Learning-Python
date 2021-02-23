print('-' * 11)
print('   BANCO')
print(('-' * 11))
valor = int(input('Que valor você quer sacar? R$'))
total = valor
totcedula = 0
ced1 = 50
while True:
    if total >= ced1:
        total -= ced1
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${ced1} ')
        if ced1 == 50:
            ced1 = 20
        elif ced1 == 20:
            ced1 = 10
        elif ced1 == 10:
            ced1 = 1
        totcedula = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado! Volte sempre!')