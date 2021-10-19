def split_by_index(s: str, indexes: list[int]) -> list[str]:
    result = []
    start = 0
    for index in indexes:
        result.append(s[start:index])
        start = index
    split = s[start:]
    if split:
        result.append(split)
    return result

def main():
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))

if __name__ == "__main__":
    main()
