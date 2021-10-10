def endless_fib_generator():
    start1, start2 = 0,1
    while True:
        yield start1
        start2 += start1
        yield start2
        start1 += start2

def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen))
if __name__ == "__main__":
    main()
