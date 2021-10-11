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

def main():
    while True:
        num = int(input())
        print(verification2(num))

if __name__ == "__main__":
    main()
