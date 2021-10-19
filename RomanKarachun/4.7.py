def foo(list) -> list:
    ls = []
    x=len(list)
    for i in range(x):
        st=1
        for j in range(x):
            if i == j:
                continue
            st *= list[j]
        ls.append(st)
    return ls
def main():
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
if __name__ == "__main__":
    main()
