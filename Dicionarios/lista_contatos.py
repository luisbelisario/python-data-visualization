contatos = {'Luis': '(87) 9876-3913',
            'Caetano': '(86) 9765-0987',
            'Paulo': '(89) 9768-9087'}


def getContato(contatos, nome):
    if nome in contatos:
        return contatos[nome]
    else:
        return 'Contato não encontrado'


def mostraContatos(contatos):
    for nome, numero in contatos.items():
        print(nome, ':', numero)


def ordemAlfabetica(contatos):
    chaves = contatos.keys()
    nomes = sorted(chaves)
    for nome in nomes:
        print(nome, ':', contatos[nome])


def addContato(contatos, nome, numero):
    if nome in contatos:
        print('Impossível adicionar! Contato já existente!')
    else:
        contatos[nome] = numero
        print('Contato adicionado com sucesso!')


def updateContato(contatos, nome, novoNumero):
    if nome in contatos:
        contatos[nome] = novoNumero
        print('Contato atualizado com sucesso!')
    else:
        print('Contato não encontrado! Tente novamente!')


print(getContato(contatos, 'Luis'))
print(getContato(contatos, 'Antônio'))

print('\nContatos da Agenda: ')
mostraContatos(contatos)


print('\nContatos em ordem alfabética: ')
ordemAlfabetica(contatos)
print()

addContato(contatos, 'Luis', '(87) 8664-5484')
addContato(contatos, 'Pedro', '(87) 86647484')
print()
updateContato(contatos, 'Luis', '(87) 8564-5484')
updateContato(contatos, 'João', '(87) 8564-5484')
