meses = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05',
         'Junho': '06', 'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10',
         'Novembro': '11', 'Dezembro': '12'
         }

dia = input('Dia: ')
mes = input('mês: ')
ano = input('Ano: ')

for m, n in meses.items():
    if n == mes:
        print(f'Você nasceu em {dia} de {m} de {ano}')
