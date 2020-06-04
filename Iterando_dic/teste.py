nested_list = [[i * row for i in range(25)] for row in range(25)]

print(nested_list)

soma = 0
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        if i == j:
            soma = soma + nested_list[i][j]


print(soma)
