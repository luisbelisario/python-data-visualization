import csv


def analisar(arquivoNome):
    tabela = []
    with open(arquivoNome, 'r') as arquivo:
        leitorCsv = csv.reader(arquivo, skipinitialspace=True)
        '''
        skipinitialspace=True se houver algum espaço vazio antes
        do dado, o progrma o ignorará
        '''
        for linha in leitorCsv:
            tabela.append(linha)
    return tabela


def printar_tabela(tabela):
    for linha in tabela:
        # colunas cabeçalho da tabela justificadas à esquerda
        print("{:<19}".format(linha[0]), end=' ')
        for coluna in linha[1:]:
            print('{:>4}'.format(coluna), end='')
        print('', end='\n')


tabela = analisar('hightemp.csv')
print(tabela)
printar_tabela(tabela)


print()
print()

tabela = analisar('hightemp2.csv')
print(tabela)
printar_tabela(tabela)
