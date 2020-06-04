def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table


def printar_tabela(tabela):
    for linha in tabela:
        # colunas cabeçalho da tabela justificadas à esquerda
        print("{:<19}".format(linha[0], end=' '))
        for coluna in linha[1:]:
            print('{:>4}'.format(coluna), end='')
        print('', end='\n')


tabela = parse('hightemp.csv')
printar_tabela(tabela)
