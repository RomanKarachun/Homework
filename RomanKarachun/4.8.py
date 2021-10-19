def get_pairs(lst: list) -> list[tuple]:
    return list(zip(lst[:-1], lst[1:]))
def main():
    print(get_pairs([ 1 , 2 , 3 , 8 , 9 ]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
if __name__ == "__main__":
    main()
