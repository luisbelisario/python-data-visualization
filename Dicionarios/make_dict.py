lista_touros = [('Baleado', 987), ('Nortão', 900), ('Trem Fantasma', 876)]


def make_dict(lista_chave_valor):
    dic1 = dict(lista_chave_valor)
    return dic1


dic_touros = make_dict(lista_touros)

print('Peso dos touros CRP:\n')

for k, v in dic_touros.items():
    print(f'{k}: {v} kg')
