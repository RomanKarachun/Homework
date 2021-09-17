stor = dict([input('Введите ключ и значение через пробел:').split() for _ in range(3)])
res = sorted(stor.items())
print(res)
