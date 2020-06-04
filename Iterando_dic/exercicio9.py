grade_table = {'Joe': {'Assign #1': 100,
                       'Assign #2': 98,
                       'Assign #3': 100,
                       'Assign #4': 13},
               'Scott': {'Assign #1': 75,
                         'Assign #2': 59,
                         'Assign #3': 89,
                         'Assign #4': 77},
               'John': {'Assign #1': 86,
                        'Assign #2': 84,
                        'Assign #3': 91,
                        'Assign #4': 78},
               }

print('Name     Assign #1       Assign #2       Assign #3       Assign #4')


for nome, nota in grade_table.items():
    linha = "{:10} {:4} {:15} {:15} {:15}".format(nome,
                                                  nota['Assign #1'],
                                                  nota['Assign #2'],
                                                  nota['Assign #3'],
                                                  nota['Assign #4'])
    print(linha)
