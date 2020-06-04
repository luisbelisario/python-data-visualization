dic1 = {1: 'Luis'}

dic2 = {}

print(len(dic1))
print(len(dic2))


def is_empty(dic):
    if len(dic) == 0:
        return 'Empty'
    else:
        return 'Not empty'


print(is_empty(dic1))
print(is_empty(dic2))
