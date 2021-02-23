''' Programa para guardar os dados dos alunos de uma escola.'''

# step1
'''O programa deve exibir um menu com as seguintes opções: 
a) Adicionar novo aluno (Cada aluno tem nome e telefone)
b) Mostrar alunos
c) sair '''

# step2
'''Adicionar mais opções ao programa
d) Pesquisar aluno por nome 
e) remover aluno'''

#step3
'''Cada aluno agora tem 3 notas, adicione as opções:
f) Adicionar 3 notas de um aluno
g) informar se o alundo está aprovado, reprovado ou é aluno novo
'''


base = list()  # Lista vazia
empty_dict = dict()  # Dicionario vazio
OPÇÕES = 'abcdefg'  # Opções de entrada para o menu de opções

individuo = dict()  # Dicionario temporário que salva nome e telefone do aluno

alunos = list()  # Lista que salva os dados dos alunos (telefone e nome)
numero = dict()  # Dicionario que associa o nome do aluno com o numero na ordem em que foi adicionado
notas = dict()  # Dicionario que salva as 3 notas de um aluno
nome_notas = dict()  # Dicionario que associa o nome do aluno com as notas


def main():  # Função que vai ser executada

    menu_de_opções()


'''sempre que houver um "print('')", o intuito foi manter a estética do programa,
 pulando uma linha para manter a legibilidade.'''


def menu_de_opções():  # Mostra o menu de opções para que o usuário possa acessar o banco de dados

    while True:

        menu()
        options = str(input('Selecione uma das opções do menu: '))

        if options in 'a':  # Adiciona um estudante caso o usuario selecione a letra 'a'

            enter_student()
            print('')

        if options in 'b':  # Mostra uma lista contendo todos os estudantes

            print('')
            show_students()
            print('')

        if options in 'c':  # Mostra os dados de um determinado estudante

            print(search())
            print('')

        if options in 'd':  # Opção para remover os dados de um estudante

            print(remove())
            print('')

        if options in 'e':  # Opção para adicionar três notas a um determinado aluno

            three_grades()
            print('')

        if options in 'f':  #  Opção que mostra se um determinado aluno foi aprovado ou não

            status()
            print('')

        if options in 'g':  # Opção para encerrar o programa

            print('')
            break

        '''Verifica se a entrada do usuário condiz com programa. caso contrário, repete o menu de opções'''
        if options not in OPÇÕES or options in '':

            print('')

    print('Programa Encerrado!')


def menu():  # Mostra na tela o menu de opções
    print(

        '''-- Menu de cadastro da escola --
    a) Adicionar novo aluno
    b) Mostrar alunos
    c) Pesquisar aluno por nome
    d) Remover aluno
    e) Adicionar 3 notas ao aluno
    f) Status do aluno
    g) Encerrar programa

            ''')


def enter_student():  # pede os dados do estudante

    nome = str(input('Nome do aluno: ')).capitalize()  # pede o nome do estudante
    telefone = (input('telefone do aluno: '))  # pede o numero do telefone
    individuo[nome] = telefone  # Adiciona os dados no dicionario 'individuo'

    '''adiciona o aluno ao dicionario de numeros, caso o dicionario esteja vazio,
    associa o aluno como numero um.'''

    if numero == empty_dict:
        numero[nome] = 1

    else:

        numero[nome] = (len(numero) + 1)
    '''Se o dicionario não estiver vazio, associa com um número a mais que o do
         aluno ateriormente adicionado atraves da condição acima'''

    alunos.append(individuo.copy())  # Copia os dados do aluno do dicionario 'individuo' e adiciona o aluno à lista 'alunos'
    individuo.clear()  # Limpa o dicionario 'individuo' para que o proximo aluno seja adicionado após a operação

    print('')
    print('Aluno adicionado com sucesso!')


def show_students():

    if alunos == base:  # compara a lista de alunos com uma lista vazia para saber se a lista contém alunos ou não
        print('Nenhum aluno cadastrado')
    else:
        for pessoa in alunos:  # Se houver alunos cadastrados na lista, printa a lista de alunos
            print(pessoa)


def search():

    if alunos == base:  # compara a lista de alunos com uma lista vazia para saber se a lista contém alunos ou não
        return 'Nenhum aluno cadastrado'

    else:
        inp = str(input('Nome do aluno: ')).capitalize()  # Pede o nome do aluno
        for nome in numero.keys():

            if nome == inp:  # Verifica se há algum aluno com o nome digitado, printa os dados do aluno se houver
                num = numero[nome] - 1
                return alunos[num]

            elif inp not in numero.keys():  # se não houver, printa que o aluno não está cadastrado

                return 'Nenhum aluno encontrado com esse nome.'


def remove():

    if alunos == base:  # compara a lista de alunos com uma lista vazia para saber se a lista contém alunos ou não
        print('Nenhum aluno cadastrado')
        print('')

    else:
        inp = str(input('Nome do aluno: ')).capitalize()  # Pede o nome do aluno

        for nome in numero.keys():

            if nome == inp:  # Verifica se há algum aluno com o nome digitado, remove os dados do aluno se houver
                num = numero[nome] - 1
                alunos.pop(num)
                return 'Aluno removido com sucesso!'

            elif inp not in numero.keys():  # se não houver, printa que o aluno não está cadastrado

                return 'Nenhum aluno encontrado com esse nome.'


def three_grades():

    if alunos == base:  # compara a lista de alunos com uma lista vazia para saber se a lista contém alunos ou não
        print('Nenhum aluno cadastrado')

    else:
        inp = str(input('Nome do aluno: ')).capitalize()

        for nome in numero.keys():

            if nome == inp:  # verifica se há algum aluno com esse nome no dicionario de "numero", se tiver adiciona 3 notas.

                for i in range(3):
                    n = int(input(f'Digite a {i + 1}ª nota: '))
                    while n > 10 or n < 0:
                        n = int(input(f'Digite a {i + 1}ª nota: '))
                    notas[f'nota {i+1}'] = n

                nome_notas[inp] = notas  # Adiciona as notas no dicionario nome_notas

                print('')
                for k, v in nome_notas[inp].items():  # Printa as notas que o aluno tirou
                    print(f'{k} - {v}')

                print('')
                print(nome_notas)
                print('')

            elif inp not in numero.keys():  # printa que não tem aluno com o nome digitado, se não houver

                print('')
                print('Nenhum aluno encontrado com esse nome.')
                break


def status():
    m = list()  # lista temporária para adicionar as notas e calcular a média de cada aluno
    if alunos == base:  # compara a lista de alunos com uma lista vazia para saber se a lista contém alunos ou não
        return 'Nenhum aluno cadastrado'

    else:
        inp = str(input('Nome do aluno: ')).capitalize()
        for nome in nome_notas.keys():

            if nome == inp:  # verifica se há algum aluno com esse nome no dicionario de "nome_notas"

                for nota in nome_notas.values():

                    for k in nota.values():  # adiciona as notas à lista "m"
                        m.append(k)

                    media = (sum(m)) / 3  # Calcula a média de valores da lista
                    print('')
                    print(f'A média de {inp} foi {media}')  # Printa a média do aluno


                    # Daqui em diante a média determina se o aluno foi aprovado ou não, ou, ainda, se é aluno novato (Não possui notas atribuidas)
                    if media > 7:
                        print(f'{inp} foi APROVADO!')

                    elif media < 7:
                        print(f'{inp} foi REPROVADO!')

                    else:
                        print(f'{inp} é aluno NOVO!')

                    print('')


if __name__ == "__main__":  # Define para rodar apenas a função "main()"
    main()
