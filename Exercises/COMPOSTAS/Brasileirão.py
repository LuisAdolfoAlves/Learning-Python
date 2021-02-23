times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atletico', 'São Paulo', \
        'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',\
        'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', \
        'Chapecoense', 'Avaí'
print('=' * 30)
print('Lista de times do Brasileirão: ', times)
print('=' * 30)
print(f'''Os 5 primeiros colocados são: 
1º {times[0]}
2º {times[1]}
3º {times[2]}
4º {times[3]}
5º {times[4]}''')
print('=' * 30)
print(f'''os 4 últimos colocados são:  
17º {times[16]}
18º {times[17]}
19º {times[18]}
20º {times[19]}''')
print('=' * 26)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 26)
print(f'O time da Chapecoense se encontra na {times.index("Chapecoense") + 1}º posição')