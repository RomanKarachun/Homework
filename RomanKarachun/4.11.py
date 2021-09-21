def combine_dicts(*args):
    dic = {}
    for arg in args:
        for key, val in arg.items():
            dic[key] = dic.get(key, 0) + val
    return dic
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
