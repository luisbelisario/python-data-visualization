import csv


def printarTabela(tabela):
    """
    Echo a nested listto the console
    """
    for linha in tabela:
        print(linha)


def lerArquivoCsv(nomeArquivo):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    with open(nomeArquivo, newline='') as arquivoCsv:
        tabela = []
        leitorCsv = csv.reader(arquivoCsv, delimiter=',')
        for linha in leitorCsv:
            tabela.append(linha)
    return tabela


def escreverArquivoCsv(tabelaCsv, nomeArquivo):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated
    CSV file with the name file_name
    """
    with open(nomeArquivo, 'w', newline='') as arquivoCsv:
        escritorCsv = csv.writer(
            arquivoCsv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for linha in tabelaCsv:
            escritorCsv.writerow(linha)


def test_part1_code():
    """
    Run examples that test the functions for part 1
    """

    # Testa o esritor
    tabelaCancer = lerArquivoCsv("cancer_risk_county.csv")
    escreverArquivoCsv(tabelaCancer, "cancer_risk_county2.csv")
    tabelaCancer2 = lerArquivoCsv("cancer_risk_county2.csv")

    # Testa se duas tabelas são iguais
    for linha in range(len(tabelaCancer)):
        for coluna in range(len(tabelaCancer[0])):
            if tabelaCancer[linha][coluna] != tabelaCancer2[linha][coluna]:
                print(f'Diferentes na linha:{linha}, coluna{coluna}')
                print(f'Tabela1: {tabelaCancer[linha][coluna]}')
                print(f'Tabela2: {tabelaCancer2[linha][coluna]}')


test_part1_code()
