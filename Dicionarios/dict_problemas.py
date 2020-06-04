'''
Recomenda-se que, ao criar um dicionário, use-se o mesmo
tipo de dados para todas as keys. Assim, se uma key for
String é recomendado que todas as outras também sejam String
'''

dic2 = {4.0: 2, 'a': 3, True: 'true', False: 'false'}

print(dic2)

dic2[1] = 7
# Atualiza o valor da key True para 7
# Isso porque p/ o Python 1 e True são equivalentes
# Ao passar a key 1 e havendo True como key, Python os trata como iguais
print(dic2)

dic2[0] = 8
# Com o 0 e False acontece a mesma coisa
print(dic2)

dic2[4] = 7
# Python não difere float e int nas chaves
# Para ele os valores 4.0 e 4 como chaves são iguais
# Portanto, não será adicionado um novo valor e sim apenas atualizado
print(dic2)

dic2['A'] = 'abc'
# Aqui foi adicionado uma nova chave porque Python é CaseSensitive
print(dic2)
