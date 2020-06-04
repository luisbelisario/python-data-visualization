my_dict = {'Luis': 'Henrique', 'Diego': 'Alves', 'Felipe': 'Luis'}


def dict_copies(dic, num):
    list = [dic for _ in range(num)]
    return list


print(dict_copies(my_dict, 3))
