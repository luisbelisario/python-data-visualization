good_dict = {("Joe", "Warren"): 1,
             ("Scott", "Rixner"): 2,
             ("John", "Greiner"): 3}
# se eu quiser usar valores multiplos como chaves do dict
# tenho que usar tupla, se eu usar lista dará erro
# unhasahble type, isso porque tuplas são imutáveis


print(good_dict[("Joe", "Warren")])
print(good_dict[("John", "Greiner")])

# teste = {[0]: 'erro'}

# print(teste[[0]])


def lookup(dict, key, default_value=None):
    if key in dict:
        return dict[key]
    else:
        return default_value
# Esse método pode ser substituído pela função get('key', 'default_value=')


simple_dict = {"Joe": 1, "Scott": 2, "John": 3}

print(lookup(simple_dict, "Joe", -1))  # 1
print(lookup(simple_dict, "Stephen", -1))  # -1
print(lookup(simple_dict, "Stephen"))  # None
