str = input("Enter the string: ")
str = str.lower()
l = len(str)
p = l-1
index = 0
while index < p:
    if str[index] == str[p]:
        index += 1
        p -= 1
        if index == p or index + 1 == p:
            print("Yes")
    else:
        print("No")
        break
