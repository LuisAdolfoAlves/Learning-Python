boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
print('-='*15)
if boletim['média'] >= 7:
    boletim['sitação'] = 'aprovado'
else:
    boletim['situação'] = 'reprovado'
for k, v in boletim.items():
    print(f'{k}: {v}')
