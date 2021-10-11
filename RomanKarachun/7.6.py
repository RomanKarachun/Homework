class func(Exception):
    pass
class lessthanorequaltotwo(func):
    pass
class notint(func):
    pass
class odd(func):
    pass

def verification1(num):
    try:
        num = int(num)
    except ValueError:
        raise notint("Not integer") from ValueError
    else:
        if num <= 2:
            raise lessthanorequaltotwo("Less than or equal to two")
        if num %2 != 0:
            raise odd("Odd number")
        return True

def verification2(num) -> bool:
    if verification1(num):
        return int(num) %2 == 0

def amount(num: int) -> list:
    primesnum = [2]
    marked = [False] * (int(num / 2) + 100)

    for x in range(1, int((num ** (0.5) - 1) / 2) + 1):
        for y in range((x * (x + 1)) << 1, int(num / 2) + 1, 2 * x + 1):
            marked[y] = True

    for x in range(1, int(num / 2)):
        if not marked[x]:
            primesnum.append(2 * x + 1)

    return primesnum

def primesnum1(primes_list, num):
    idx = 0
    while primes_list[idx] <= num // 2:
        diff = num - primes_list[idx]
        if diff in primes_list:
            return f"{primes_list[idx]} + {diff}"
        idx += 1


def goldbach(num):
    if verification2(num):
        num = int(num)
        primes_list = amount(num)
        return primesnum1(primes_list=primes_list, num=num)

def main():
    while True:
        num = int(input("enter num; q = successfully close"))
        if num == "q":
            break
        try:
            print(goldbach(num))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    main()
