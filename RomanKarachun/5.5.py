def remember_result(func):
    def lrof(*args):
        print(f"Last result = '{lrof.cash}'")
        lrof.cash = func(*args)
        return lrof.cash
    lrof.cash = None
    return lrof
@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        if isinstance(item, int):
            result = sum(args)
            break
        result += item
    print(f"Current result = '{result}'")
    return result
def main():
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
if __name__ == "__main__":
    main()
