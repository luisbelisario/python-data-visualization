"""
Tabular data as a nested list.
"""

popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
              ["Java", 1, 2, 1, 1, 15, 0, 0],
              ["C", 2, 1, 2, 2, 1, 1, 1],
              ["C++", 3, 3, 3, 3, 2, 2, 5],
              ["C#", 4, 4, 7, 13, 0, 0, 0],
              ["Python", 5, 7, 6, 11, 27, 0, 0],
              ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
              ["PHP", 7, 6, 4, 5, 0, 0, 0],
              ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
              ["Perl", 9, 8, 5, 4, 4, 10, 0]]

format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"

cabecalho = popularity[0]
linha_cabecalho = format_string.format(*cabecalho)
'''
O metodo format() pega vários argumentos e passa cada um deles
para um dos campos da string format_string. Assim, Language vai
ficar com {:<20}, 2017 com {:>4} e assim por diante. Assim o
* possibilita usar uma lista em vez de usar apenas um argumento.
Com o * estão dizendo ao Python para ele aplicar aquele método
em cada um dos elementos da lista.
'''
print(linha_cabecalho)
print("-" * len(linha_cabecalho))

for language in popularity[1:]:
    print(format_string.format(*language))

print()

# Encontrando itens específicos
print(f'Popularidade do Python em 1997: {popularity[5][5]}')

print()


def procuraAno(tabela, ano):
    '''
    retorna o indice da coluna/ano passada como parâmetro
    se ela existir na tabela, ou retorna -1 caso essa
    coluna/ano não exista.
    '''
    if ano in tabela[0]:
        return tabela[0].index(ano)
    else:
        return -1


def procuraLinguagem(tabela, linguagem):
    '''
    retorna o indice da linha/linguagem passada como parâmetro
    se ela existir na tabela, ou retorna -1 caso essa
    linha/linguagem não exista.
    '''
    for id in range(len(tabela)):
        if tabela[id][0] == linguagem:
            return id
    return -1


print(procuraAno(popularity, 2007))  # 3
print(procuraAno(popularity, 1988))  # -1
print(procuraLinguagem(popularity, 'Python'))  # 5
print(procuraLinguagem(popularity, 'Kotlin'))  # -1

idxPython = procuraLinguagem(popularity, 'Python')
idx1997 = procuraAno(popularity, 1997)

print(f'Popularidade do Python em 1997: {popularity[5][5]}')
