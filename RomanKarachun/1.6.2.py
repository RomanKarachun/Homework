a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
d = int(input("d= ")) 
for i in range(a, b+1) :
    for j in range(c, d+1):
        print(str(i*j).rjust(4),end=" ")
print()
print()
