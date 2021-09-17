items = input("Введите последовательность слов, разделенных запятыми: ")
words = sorted(set(items.split(',')))
print (words)
