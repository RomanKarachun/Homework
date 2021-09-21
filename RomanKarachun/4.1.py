def kov(string):
    sym = [x for x in string]
    for i in range(len(sym)):
        if sym[i] == "\'":
            sym[i] = "\""
        elif sym[i] == "\"":
            sym[i] = "\'"
    return ''.join(sym)
a = input()
print(kov(a))
