nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print('''Tirando as notas {:.1f} e {:.1f}, a media é {:.1f}
Portanto o aluno está {}APROVADO{}'''.format(nota1, nota2, media, '\033[4;32m', '\033[m'))
elif media >= 4 and media < 6:
    print('''Tirando as notas {:.1f} e {:.1f}, a media é {:.1f}
Portanto o aluno está em {}RECUPERAÇÃO{}'''.format(nota1, nota2, media,'\033[4;31m', '\033[4m'))
elif media < 4:
    print('''Tirando as notas {:.1f} e {:.1f}, a media é {:.1f}
Portanto o aluno está {}REPROVADO{}'''.format(nota1, nota2, media,'\033[4;31m', '\033[4m'))

