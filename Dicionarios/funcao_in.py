"""
Checking for keys in a dictionary.
"""

print("Usando 'in': \n")
'''
Usamos 'in' para verficar de uma key está no dicionário
'''

dic1 = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
print(1 in dic1)  # True
print(8 in dic1)  # True

# Values - o 'in' não detecta values, apenas keys
print(5 in dic1)  # False
print(-3 in dic1)  # False

# Ambos
print(22 in dic1)  # True, pois 22 também é uma key

# Nenhum
print(82 in dic1)  # False

print("\nUsando 'in' para prevenir erros: \n")

keys = [8, 14, 22, 25]

for key in keys:
    if key in dic1:
        print(f'{key}: {dic1[key]}')
    else:
        print(f'A chave {key} não está no dicionário')
