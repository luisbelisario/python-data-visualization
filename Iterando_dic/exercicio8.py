def make_dict_lists(length):
    dic = {}
    for i in range(length):
        dic[i] = [0] * i
    return dic


print(make_dict_lists(3))
