str1 = input("Введите строку: ")
kolvo = {}
str1 = str1.lower()
for x in str1:
    if x in kolvo:
        kolvo[x] += 1
    else:
        kolvo[x] = 1 
print (str(kolvo))
