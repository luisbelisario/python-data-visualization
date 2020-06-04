nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]

print(nested_list)

for row in range(len(nested_list)):
    for col in range(len(nested_list[row])):
        if nested_list[row][col] == 7:
            print('Dados do 7')
            print(f'Linha: {row}')
            print(f'Coluna: {col}')
