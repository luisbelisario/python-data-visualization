import csv


MESES = ('Jan', 'Feb', 'Mar', 'Apr',
         'May', 'Jun', 'Jul', 'Aug',
         'Sep', 'Oct', 'Nov', 'Dec')


def analisaDict(arquivoNome, chave):
    tabela = {}
    with open(arquivoNome, 'rt', newline='') as arquivo:
        leitorCsv = csv.DictReader(arquivo, skipinitialspace=True)
        for linha in leitorCsv:
            tabela[linha[chave]] = linha
    return tabela


def printar_tabela(tabela):
    print("City              ", end=' ')
    for mes in MESES:
        print("{:>6}".format(mes), end='')
    print("")
    for cidade, dados in tabela.items():
        # Header column left justified
        print("{:<19}".format(cidade), end='')
        # Remaining columns right justified
        for mes in MESES:
            print("{:>6}".format(dados[mes]), end='')
        print()


tabela = analisaDict('hightemp.csv', 'City')
print(tabela)
printar_tabela(tabela)

tabela = analisaDict('hightemp2.csv', 'City')
print(tabela)
printar_tabela(tabela)
