def split_by_index(num: int) -> tuple[int]:
    return tuple(int(num) for num in str(num))
def main():
    print(split_by_index(87178291199))
if __name__ == "__main__":
    main()
