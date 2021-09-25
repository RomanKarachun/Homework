def call_once(func):
    def cash(*args, **kwargs):
        if cash.result is None:
            cash.result = func(*args, **kwargs)
        return cash.result
    cash.result = None
    return cash
@call_once
def sum_of_numbers(a, b):
    return a + b
def main():
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))
if __name__ == "__main__":
    main()
