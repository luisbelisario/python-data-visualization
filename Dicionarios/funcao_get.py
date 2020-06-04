print('Dictonary Lookup')


cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'}
print(cipher)

# Acesso através das keys
print(cipher['t'])
print(cipher['n'])


# Encriptando o dicionário
def encrypt(cipher, word):
    """criptografa a palavra usando cipher"""
    crypto = ''
    for c in word:
        crypto += cipher[c]
    return crypto


encrypted = encrypt(cipher, 'python')
print('python', encrypted)

# print(cipher[1]) - erro, pois não existe essa key no dict (KeyError)

# Use o método .get() se você não tem ctz se aquela key existe
print(cipher.get('t'))  # n
print(cipher.get(1))  # None
print(cipher.get(1, 'Chave não encontrada'))
# essa ultima função retorna um valor padrão caso não haja aquela key no dict
# usa-se pq pode haver valores None inclusos no dict, geraria confusão
print(cipher.get('p', 'Chave não encontrada'))
