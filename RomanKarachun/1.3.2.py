list1 = []
number = int(input("Введите число: "))
for element in range (1, (number + 1)):
        if number % element == 0:
            list1.append(element)
print(list1)
