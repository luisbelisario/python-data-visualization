print('Creating Dcitionaries:\n')

empty1 = {}  # curly brace

empty = dict()
print(empty)

data = [(1, 'one'), (2, 'two'), (3, 'three')]
'''
Se eu passar uma sequencia, essa sequencia tem
que ser um par de elementos, para que o interpretador
os tranforme em pares key: value
'''
names = dict(data)
print(names)

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'}
print(cipher)
cipher2 = dict(cipher)
print(cipher2)
